from rest_framework import serializers


from apps.blog.models import (
    Post,
    PostImage,
    Tag,
)





class TagSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Tag

        fields = [
            "id",
            "name",
            "slug",
        ]





class PostImageSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = PostImage

        fields = [
            "id",
            "image",
            "alt_text",
            "order",
        ]





class PostSerializer(
    serializers.ModelSerializer
):

    author = serializers.EmailField(
        source="author.email",
        read_only=True,
    )


    tags = TagSerializer(
        many=True,
        read_only=True,
    )


    images = PostImageSerializer(
        many=True,
        read_only=True,
    )



    class Meta:

        model = Post

        fields = [
            "id",
            "title",
            "slug",
            "content",
            "status",
            "author",
            "tags",
            "images",
            "published_at",
            "created_at",
            "updated_at",
        ]


        read_only_fields = [
            "id",
            "slug",
            "author",
            "created_at",
            "updated_at",
        ]





class PostCreateSerializer(
    serializers.Serializer
):

    title = serializers.CharField(
        max_length=200,
    )


    content = serializers.CharField()


    status = serializers.ChoiceField(
        choices=Post.Status.choices,
        default=Post.Status.DRAFT,
    )


    tags = serializers.ListField(
        child=serializers.CharField(
            max_length=100,
        ),
        required=False,
        default=list,
    )


    published_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
    )



    def validate_title(
        self,
        value,
    ):

        value = value.strip()


        if not value:

            raise serializers.ValidationError(
                "Title cannot be empty."
            )


        return value
