from django.conf import settings
from django.db import models
from django.utils.text import slugify



class Tag(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )


    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
    )



    class Meta:

        ordering = [
            "name",
        ]



    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(
                self.name,
                allow_unicode=True,
            )

        super().save(*args, **kwargs)



    def __str__(self):

        return self.name







class Post(models.Model):


    class Status(models.TextChoices):

        DRAFT = "draft", "پیش‌نویس"

        PUBLISHED = "published", "منتشر شده"

        ARCHIVED = "archived", "آرشیو شده"




    title = models.CharField(

        max_length=200,

    )


    slug = models.SlugField(

        max_length=220,

        unique=True,

        blank=True,

    )


    content = models.TextField()



    status = models.CharField(

        max_length=20,

        choices=Status.choices,

        default=Status.DRAFT,

    )



    author = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name="posts",

    )



    tags = models.ManyToManyField(

        Tag,

        blank=True,

        related_name="posts",

    )



    published_at = models.DateTimeField(

        null=True,

        blank=True,

    )



    created_at = models.DateTimeField(

        auto_now_add=True,

    )


    updated_at = models.DateTimeField(

        auto_now=True,

    )





    class Meta:

        ordering = [

            "-created_at",

        ]


        indexes = [

            models.Index(

                fields=[

                    "status",

                    "-created_at",

                ],

            ),

        ]





    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(

                self.title,

                allow_unicode=True,

            )


        super().save(*args, **kwargs)





    def __str__(self):

        return self.title







class PostImage(models.Model):


    post = models.ForeignKey(

        Post,

        on_delete=models.CASCADE,

        related_name="images",

    )



    image = models.ImageField(

        upload_to="blog/images/",

    )



    alt_text = models.CharField(

        max_length=200,

        blank=True,

    )



    order = models.PositiveIntegerField(

        default=0,

    )





    class Meta:

        ordering = [

            "order",

        ]





    def __str__(self):

        return f"{self.post.title} image"
