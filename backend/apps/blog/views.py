from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
)


from apps.blog.models import (
    Post,
    PostImage,
)


from apps.blog.serializers import (
    PostSerializer,
    PostCreateSerializer,
)


from apps.blog.permissions import (
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

        user = self.request.user


        if (

            user.is_authenticated

            and user.is_superuser

        ):

            return Post.objects.all()



        return Post.objects.filter(

            status=Post.Status.PUBLISHED

        )





    def get_serializer_class(self):

        if self.action == "create":

            return PostCreateSerializer


        return PostSerializer





    def perform_create(self, serializer):


        self.created_post = serializer.save(

            author=self.request.user

        )



        images = self.request.FILES.getlist(

            "images"

        )


        for index, image in enumerate(images):


            PostImage.objects.create(

                post=self.created_post,

                image=image,

                order=index,

            )





    def create(self, request, *args, **kwargs):


        serializer = self.get_serializer(

            data=request.data

        )


        serializer.is_valid(

            raise_exception=True

        )


        self.perform_create(

            serializer

        )



        output_serializer = PostSerializer(

            self.created_post,

            context={

                "request": request

            }

        )


        return Response(

            output_serializer.data,

            status=status.HTTP_201_CREATED

        )
