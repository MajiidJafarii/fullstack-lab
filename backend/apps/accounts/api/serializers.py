from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from apps.accounts.models import User


# =============================================================================
# User
# =============================================================================


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "email_verified",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
        ]

        read_only_fields = [
            "id",
            "email",
            "email_verified",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
        ]


# =============================================================================
# Register
# =============================================================================


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()

    first_name = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=True,
    )

    last_name = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=True,
    )

    password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    password_confirm = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(
            email__iexact=email
        ).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )

        return email

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.get(
            "password_confirm"
        )

        if password != password_confirm:
            raise serializers.ValidationError(
                {
                    "password_confirm": (
                        "Passwords do not match."
                    )
                }
            )

        temporary_user = User(
            email=attrs.get("email"),
            first_name=attrs.get(
                "first_name",
                "",
            ),
            last_name=attrs.get(
                "last_name",
                "",
            ),
        )

        validate_password(
            password,
            user=temporary_user,
        )

        return attrs

    def create(self, validated_data):
        validated_data.pop(
            "password_confirm"
        )

        password = validated_data.pop(
            "password"
        )

        user = User.objects.create_user(
            password=password,
            email=validated_data.pop(
                "email"
            ),
            is_active=False,
            email_verified=False,
            **validated_data,
        )

        return user


# =============================================================================
# Login
# =============================================================================


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    def validate_email(self, value):
        return value.strip().lower()


# =============================================================================
# Email verification
# =============================================================================


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    code = serializers.RegexField(
        regex=r"^\d{6}$",
        min_length=6,
        max_length=6,
    )

    def validate_email(self, value):
        return value.strip().lower()


class ResendVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        return value.strip().lower()


# =============================================================================
# Profile
# =============================================================================


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
        ]


# =============================================================================
# Change password
# =============================================================================


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    new_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    new_password_confirm = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    def validate(self, attrs):
        new_password = attrs.get(
            "new_password"
        )

        new_password_confirm = attrs.get(
            "new_password_confirm"
        )

        if (
            new_password
            != new_password_confirm
        ):
            raise serializers.ValidationError(
                {
                    "new_password_confirm": (
                        "Passwords do not match."
                    )
                }
            )

        request = self.context.get(
            "request"
        )

        user = (
            request.user
            if request
            else None
        )

        validate_password(
            new_password,
            user=user,
        )

        return attrs
