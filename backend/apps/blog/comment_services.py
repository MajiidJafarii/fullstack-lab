from apps.blog.models import Comment



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

        is_approved=False,

    )





def approve_comment(

    comment,

):

    comment.is_approved = True

    comment.save(

        update_fields=[

            "is_approved"

        ]

    )

    return comment





def hide_comment(

    comment,

):

    comment.is_approved = False

    comment.save(

        update_fields=[

            "is_approved"

        ]

    )

    return comment
