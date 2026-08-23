import secrets
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.db import transaction
from django.utils import timezone

from apps.accounts.models import EmailVerificationCode, User


CODE_TTL_MINUTES = 10
RESEND_COOLDOWN_SECONDS = 60
MAX_ATTEMPTS = 5


# =============================================================================
# Exceptions
# =============================================================================


class EmailVerificationError(Exception):
    pass


class EmailAlreadyVerifiedError(EmailVerificationError):
    pass


class VerificationCodeCooldownError(EmailVerificationError):
    def __init__(self, seconds_remaining: int):
        self.seconds_remaining = seconds_remaining

        super().__init__(
            f"Please wait {seconds_remaining} seconds "
            f"before requesting another code."
        )


class VerificationCodeInvalidError(EmailVerificationError):
    pass


class VerificationCodeExpiredError(EmailVerificationError):
    pass


class VerificationCodeAttemptsExceededError(
    EmailVerificationError
):
    pass


# =============================================================================
# Generate code
# =============================================================================


def generate_verification_code() -> str:
    """
    Generate a cryptographically secure 6-digit code.
    """

    return f"{secrets.randbelow(1_000_000):06d}"


# =============================================================================
# Cooldown
# =============================================================================


def _check_resend_cooldown(user: User) -> None:
    latest_code = (
        EmailVerificationCode.objects
        .filter(user=user)
        .order_by("-created_at")
        .first()
    )

    if latest_code is None:
        return

    allowed_at = (
        latest_code.created_at
        + timedelta(
            seconds=RESEND_COOLDOWN_SECONDS
        )
    )

    now = timezone.now()

    if now < allowed_at:
        remaining = int(
            (
                allowed_at - now
            ).total_seconds()
        ) + 1

        raise VerificationCodeCooldownError(
            seconds_remaining=remaining
        )


# =============================================================================
# Send verification code
# =============================================================================


@transaction.atomic
def send_verification_code(
    user: User,
) -> None:
    """
    Generate, hash, store and send
    a new email verification code.
    """

    if user.email_verified:
        raise EmailAlreadyVerifiedError(
            "Email is already verified."
        )

    _check_resend_cooldown(
        user
    )

    now = timezone.now()

    # تمام کدهای قبلی کاربر باطل شوند
    EmailVerificationCode.objects.filter(
        user=user,
        used_at__isnull=True,
    ).update(
        used_at=now
    )

    code = (
        generate_verification_code()
    )

    # کد خام داخل دیتابیس ذخیره نمی‌شود
    EmailVerificationCode.objects.create(
        user=user,
        code_hash=make_password(
            code
        ),
        expires_at=(
            now
            + timedelta(
                minutes=CODE_TTL_MINUTES
            )
        ),
    )

    # در Development داخل Terminal چاپ می‌شود
    send_mail(
        subject="Email verification code",

        message=(
            "Your verification code is:\n\n"
            f"{code}\n\n"
            "This code expires in "
            f"{CODE_TTL_MINUTES} minutes."
        ),

        from_email=(
            settings.DEFAULT_FROM_EMAIL
        ),

        recipient_list=[
            user.email,
        ],

        fail_silently=False,
    )


# =============================================================================
# Verify email code
# =============================================================================


def verify_email_code(
    user: User,
    code: str,
) -> User:
    """
    Validate the latest active verification code.

    Important:
    Database changes must be committed BEFORE
    domain exceptions are raised.

    Otherwise transaction rollback would undo:
    - attempts increment
    - expiration marking
    - used_at changes
    """

    if user.email_verified:
        return user

    error_to_raise = None

    with transaction.atomic():
        verification = (
            EmailVerificationCode.objects
            .select_for_update()
            .filter(
                user=user,
                used_at__isnull=True,
            )
            .order_by(
                "-created_at"
            )
            .first()
        )

        # ---------------------------------------------------------------------
        # No active code
        # ---------------------------------------------------------------------

        if verification is None:
            error_to_raise = (
                VerificationCodeInvalidError(
                    "No active verification code exists."
                )
            )

        else:
            now = timezone.now()

            # -----------------------------------------------------------------
            # Expired
            # -----------------------------------------------------------------

            if (
                verification.expires_at
                <= now
            ):
                verification.used_at = now

                verification.save(
                    update_fields=[
                        "used_at",
                    ]
                )

                error_to_raise = (
                    VerificationCodeExpiredError(
                        "Verification code has expired."
                    )
                )

            # -----------------------------------------------------------------
            # Attempts already exceeded
            # -----------------------------------------------------------------

            elif (
                verification.attempts
                >= MAX_ATTEMPTS
            ):
                verification.used_at = now

                verification.save(
                    update_fields=[
                        "used_at",
                    ]
                )

                error_to_raise = (
                    VerificationCodeAttemptsExceededError(
                        "Maximum verification attempts exceeded."
                    )
                )

            # -----------------------------------------------------------------
            # Wrong code
            # -----------------------------------------------------------------

            elif not check_password(
                code,
                verification.code_hash,
            ):
                verification.attempts += 1

                update_fields = [
                    "attempts",
                ]

                if (
                    verification.attempts
                    >= MAX_ATTEMPTS
                ):
                    verification.used_at = now

                    update_fields.append(
                        "used_at"
                    )

                    error_to_raise = (
                        VerificationCodeAttemptsExceededError(
                            "Maximum verification attempts exceeded."
                        )
                    )

                else:
                    error_to_raise = (
                        VerificationCodeInvalidError(
                            "Verification code is invalid."
                        )
                    )

                verification.save(
                    update_fields=update_fields
                )

            # -----------------------------------------------------------------
            # Correct code
            # -----------------------------------------------------------------

            else:
                verification.used_at = now

                verification.save(
                    update_fields=[
                        "used_at",
                    ]
                )

                user.email_verified = True
                user.is_active = True

                user.save(
                    update_fields=[
                        "email_verified",
                        "is_active",
                    ]
                )

    # =========================================================================
    # Transaction has successfully committed here.
    # Now it is safe to raise the error.
    # =========================================================================

    if error_to_raise is not None:
        raise error_to_raise

    return user
