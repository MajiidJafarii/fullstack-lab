from django.core.management.base import BaseCommand

from apps.accounts.models import User



class Command(BaseCommand):

    help = "Create test users"


    def handle(self, *args, **options):

        password = "@Aa123456"


        created = 0


        for i in range(1, 101):

            email = f"a{i}@aaaaa.aaa"


            if User.objects.filter(
                email=email
            ).exists():

                continue


            user = User(

                email=email,

                is_active=True,

                email_verified=True,

            )


            user.set_password(
                password
            )


            user.save()


            created += 1



        self.stdout.write(

            self.style.SUCCESS(

                f"{created} users created"

            )

        )
