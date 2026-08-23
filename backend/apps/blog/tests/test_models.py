from django.test import TestCase

from apps.blog.models import (
    Tag,
    Post,
)

from apps.accounts.models import User



class BlogModelTest(TestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            email="admin@test.com",
            password="password123",
        )



    def test_create_tag(self):

        tag = Tag.objects.create(
            name="Django",
        )


        self.assertEqual(
            tag.name,
            "Django",
        )



    def test_create_post(self):

        post = Post.objects.create(
            title="First Post",
            content="Hello",
            author=self.user,
        )


        self.assertEqual(
            post.author.email,
            "admin@test.com",
        )
