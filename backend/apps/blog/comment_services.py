from django.db import transaction


from apps.blog.models import Comment





@transaction.atomic
def create_comment(

    *,

    post,

    user,

    content,

):

    return Comment.objects.create(

        post=post,

        user=user,

        content=content,

    )





@transaction.atomic
def approve_comment(

    comment,

):

    comment.is_approved = True

    comment.save(
        update_fields=[
            "is_approved",
            "updated_at",
        ]
    )


    return comment
