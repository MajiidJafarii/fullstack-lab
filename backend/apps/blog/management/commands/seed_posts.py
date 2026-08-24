import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker


from apps.accounts.models import User
from apps.blog.models import Post, Tag



fake = Faker("fa_IR")



class Command(BaseCommand):

    help = "Create fake blog posts"



    def add_arguments(self, parser):

        parser.add_argument(
            "--count",
            type=int,
            default=1000,
        )



    def handle(self, *args, **options):

        count = options["count"]


        users = list(
            User.objects.filter(
                is_active=True
            )
        )


        if not users:

            self.stdout.write(
                self.style.ERROR(
                    "No users found"
                )
            )

            return



        tags = []


        tag_names = [

            "django",
            "react",
            "python",
            "typescript",
            "backend",
            "frontend",
            "database",
            "docker",
            "ai",
            "machine-learning",

        ]



        for name in tag_names:

            tag, _ = Tag.objects.get_or_create(
                name=name,
            )

            tags.append(tag)





        posts = []


        for _ in range(count):

            post = Post(

                title=fake.sentence(
                    nb_words=6
                ),

                content=fake.text(
                    max_nb_chars=500
                ),

                status=random.choice(

                    [
                        Post.Status.PUBLISHED,
                        Post.Status.PUBLISHED,
                        Post.Status.DRAFT,
                    ]

                ),

                author=random.choice(
                    users
                ),

            )


            post.save()


            post.tags.set(

                random.sample(
                    tags,
                    k=random.randint(
                        1,
                        4
                    )
                )

            )


            posts.append(post)



        self.stdout.write(

            self.style.SUCCESS(

                f"{len(posts)} posts created successfully"

            )

        )
