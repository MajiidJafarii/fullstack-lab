from rest_framework import serializers


from apps.blog.models import (
    Tag,
    Post,
    PostImage,
)





class TagSerializer(serializers.ModelSerializer):


    class Meta:

        model = Tag

        fields = [
            "id",
            "name",
            "slug",
        ]







class PostImageSerializer(serializers.ModelSerializer):


    class Meta:

        model = PostImage

        fields = [
            "id",
            "image",
            "alt_text",
            "order",
        ]







class PostSerializer(serializers.ModelSerializer):


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









class PostCreateSerializer(serializers.ModelSerializer):


    id = serializers.IntegerField(

        read_only=True,

    )


    tags = serializers.ListField(

        child=serializers.CharField(

            max_length=100

        ),

        required=False,

    )



    class Meta:

        model = Post


        fields = [
            "id",
            "title",
            "content",
            "status",
            "tags",
            "published_at",
        ]





    def create(self, validated_data):


        tags_data = validated_data.pop(

            "tags",

            []

        )



        post = Post.objects.create(

            **validated_data

        )



        for tag_name in tags_data:


            tag, _ = Tag.objects.get_or_create(

                name=tag_name,

                defaults={

                    "slug": tag_name.lower().replace(

                        " ",

                        "-"

                    )

                }

            )


            post.tags.add(tag)



        return post
