import django_filters


from apps.blog.models import Post





class PostFilter(
    django_filters.FilterSet
):


    created_after = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
    )


    created_before = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
    )



    published_after = django_filters.DateTimeFilter(
        field_name="published_at",
        lookup_expr="gte",
    )


    published_before = django_filters.DateTimeFilter(
        field_name="published_at",
        lookup_expr="lte",
    )



    class Meta:

        model = Post


        fields = [

            "status",

            "author",

            "created_after",

            "created_before",

            "published_after",

            "published_before",

        ]
