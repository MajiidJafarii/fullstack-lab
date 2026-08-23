from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import QueryDict
from django.utils.datastructures import MultiValueDict


from rest_framework import status
from rest_framework.test import APITestCase


from apps.accounts.models import User


from apps.blog.models import (
    Post,
    PostImage,
)





class BlogAPITest(APITestCase):


    def setUp(self):

        self.user = User.objects.create_user(
            email="user@test.com",
            password="password123",
        )


        self.admin = User.objects.create_superuser(
            email="admin@test.com",
            password="password123",
        )


        Post.objects.create(
            title="Public Post",
            content="public content",
            status=Post.Status.PUBLISHED,
            author=self.admin,
        )


        Post.objects.create(
            title="Draft Post",
            content="draft content",
            status=Post.Status.DRAFT,
            author=self.admin,
        )




    def test_public_user_only_sees_published_posts(self):

        response = self.client.get(
            "/api/blog/posts/"
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )


        self.assertEqual(
            len(response.data),
            1,
        )




    def test_normal_user_cannot_create_post(self):

        self.client.force_authenticate(
            user=self.user
        )


        response = self.client.post(
            "/api/blog/posts/",
            {
                "title": "User Post",
                "content": "test",
                "status": "published",
            },
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )




    def test_superuser_can_create_post(self):

        self.client.force_authenticate(
            user=self.admin
        )


        response = self.client.post(
            "/api/blog/posts/",
            {
                "title": "Admin Post",
                "content": "hello",
                "status": "published",
            },
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )


        self.assertEqual(
            response.data["title"],
            "Admin Post",
        )




    def test_superuser_can_create_post_with_tags(self):

        self.client.force_authenticate(
            user=self.admin
        )


        response = self.client.post(
            "/api/blog/posts/",
            {
                "title": "Tagged Post",
                "content": "with tags",
                "status": "published",
                "tags": [
                    "Django",
                    "Backend",
                ],
            },
            format="multipart",
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )


        post = Post.objects.get(
            title="Tagged Post"
        )


        self.assertEqual(
            post.tags.count(),
            2,
        )




    def test_superuser_can_create_post_with_images(self):

        self.client.force_authenticate(
            user=self.admin
        )


        image1 = SimpleUploadedFile(
            "image1.jpg",
            b"fake-image-content-1",
            content_type="image/jpeg",
        )


        image2 = SimpleUploadedFile(
            "image2.jpg",
            b"fake-image-content-2",
            content_type="image/jpeg",
        )


        data = {

            "title": "Post With Images",

            "content": "image content",

            "status": "published",

        }


        files = MultiValueDict({

            "images": [
                image1,
                image2,
            ]

        })



        data.update(files)



        response = self.client.post(

            "/api/blog/posts/",

            data,

            format="multipart",

        )


        self.assertEqual(

            response.status_code,

            status.HTTP_201_CREATED,

        )


        post = Post.objects.get(

            title="Post With Images"

        )


        self.assertEqual(

            post.images.count(),

            2,

        )


        self.assertEqual(

            PostImage.objects.filter(

                post=post

            ).count(),

            2,

        )
