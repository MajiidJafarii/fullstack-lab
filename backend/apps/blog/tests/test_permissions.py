from django.test import TestCase

from rest_framework.test import APIRequestFactory

from apps.blog.permissions import (
    IsSuperUserOrReadOnly,
)



class PermissionTest(TestCase):


    def test_read_is_allowed(self):

        factory = APIRequestFactory()

        request = factory.get(
            "/api/blog/posts/"
        )

        permission = IsSuperUserOrReadOnly()


        self.assertTrue(
            permission.has_permission(
                request,
                None,
            )
        )
