from drf_spectacular.utils import extend_schema


from rest_framework import status
from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from apps.blog.models import Post


from apps.blog.serializers import (
    PostCreateSerializer,
    PostSerializer,
)


from apps.blog.services import (
    create_post,
)


from apps.common.permissions import (
    IsSuperUserOrReadOnly,
)





class PostViewSet(ModelViewSet):

    permission_classes = [
        IsSuperUserOrReadOnly,
    ]


    parser_classes = [
        MultiPartParser,
        FormParser,
    ]



    def get_queryset(self):

        queryset = (
            Post.objects
            .select_related(
                "author"
            )
            .prefetch_related(
                "tags",
                "images",
            )
        )


        user = self.request.user


        if (
            user.is_authenticated
            and user.is_superuser
        ):

            return queryset


        return queryset.filter(
            status=Post.Status.PUBLISHED
        )



    def get_serializer_class(self):

        if self.action == "create":

            return PostCreateSerializer


        return PostSerializer



    @extend_schema(
        request=PostCreateSerializer,
        responses={
            201: PostSerializer,
        },
    )
    def create(
        self,
        request,
        *args,
        **kwargs,
    ):

        serializer = (
            PostCreateSerializer(
                data=request.data
            )
        )


        serializer.is_valid(
            raise_exception=True
        )


        post = create_post(
            author=request.user,
            validated_data=(
                serializer.validated_data
            ),
            images=(
                request.FILES.getlist(
                    "images"
                )
            ),
        )


        output_serializer = (
            PostSerializer(
                post,
                context={
                    "request": request,
                },
            )
        )


        return Response(
            output_serializer.data,
            status=(
                status.HTTP_201_CREATED
            ),
        )
