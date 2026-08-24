from rest_framework.viewsets import ModelViewSet


from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)


from rest_framework.response import Response


from rest_framework import status



from apps.blog.models import Comment


from apps.blog.serializers import (
    CommentSerializer,
)


from apps.blog.comment_services import (
    create_comment,
)





class CommentViewSet(
    ModelViewSet
):


    serializer_class = CommentSerializer



    permission_classes = [

        IsAuthenticatedOrReadOnly,

    ]





    def get_queryset(self):

        return (

            Comment.objects

            .filter(

                is_approved=True

            )

            .select_related(

                "user",

                "post",

            )

        )







    def perform_create(

        self,

        serializer,

    ):


        self.comment = create_comment(

            post=

                serializer.validated_data[
                    "post"
                ],


            user=

                self.request.user,


            content=

                serializer.validated_data[
                    "content"
                ],

        )





    def create(

        self,

        request,

        *args,

        **kwargs,

    ):


        serializer = CommentSerializer(

            data=request.data

        )



        serializer.is_valid(

            raise_exception=True

        )



        self.perform_create(

            serializer

        )



        output = CommentSerializer(

            self.comment,

            context={

                "request": request

            }

        )



        return Response(

            output.data,

            status=status.HTTP_201_CREATED,

        )
