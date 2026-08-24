from django.utils.text import slugify


def generate_unique_slug(
    instance,
    value: str,
    slug_field: str = "slug",
) -> str:

    model_class = instance.__class__

    field = model_class._meta.get_field(
        slug_field
    )

    max_length = field.max_length or 255


    base_slug = slugify(
        value,
        allow_unicode=True,
    )


    if not base_slug:
        base_slug = "item"


    base_slug = base_slug[
        :max_length
    ]


    queryset = model_class.objects.all()


    if instance.pk:
        queryset = queryset.exclude(
            pk=instance.pk
        )


    slug = base_slug
    counter = 1


    while queryset.filter(
        **{
            slug_field: slug,
        }
    ).exists():

        suffix = f"-{counter}"

        trimmed_base = base_slug[
            :max_length - len(suffix)
        ]

        slug = (
            f"{trimmed_base}{suffix}"
        )

        counter += 1


    return slug
