from rest_framework.permissions import BasePermission


class IsSuperUserOrReadOnly(BasePermission):
    """
    کاربران فقط خواندن دارند.
    فقط SuperUser می‌تواند تغییر ایجاد کند.
    """


    def has_permission(self, request, view):

        if request.method in [
            "GET",
            "HEAD",
            "OPTIONS",
        ]:
            return True


        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )
