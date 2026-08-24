from django.db import transaction


from apps.blog.models import (
    Post,
    PostImage,
    Tag,
)





def get_or_create_tag(
    name: str,
) -> Tag:

    clean_name = " ".join(
        name.split()
    ).strip()


    tag = Tag.objects.filter(
        name__iexact=clean_name
    ).first()


    if tag:
        return tag


    return Tag.objects.create(
        name=clean_name
    )





@transaction.atomic
def create_post(
    *,
    author,
    validated_data,
    images=None,
) -> Post:

    data = dict(
        validated_data
    )


    tag_names = data.pop(
        "tags",
        [],
    )


    post = Post.objects.create(
        author=author,
        **data,
    )


    seen_tags = set()


    for tag_name in tag_names:

        clean_name = " ".join(
            tag_name.split()
        ).strip()


        if not clean_name:
            continue


        normalized_name = (
            clean_name.casefold()
        )


        if normalized_name in seen_tags:
            continue


        seen_tags.add(
            normalized_name
        )


        tag = get_or_create_tag(
            clean_name
        )


        post.tags.add(
            tag
        )


    for index, image in enumerate(
        images or []
    ):

        PostImage.objects.create(
            post=post,
            image=image,
            order=index,
        )


    return post
