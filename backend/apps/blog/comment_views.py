from rest_framework.viewsets import ModelViewSet


from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)


from rest_framework.decorators import action


from rest_framework.response import Response


from rest_framework import status





from apps.blog.models import Comment



from apps.blog.serializers import (
    CommentSerializer,
)



from apps.blog.comment_services import (
    create_comment,
    approve_comment,
)



from apps.blog.permissions import (
    IsSuperUser,
)








class CommentViewSet(
    ModelViewSet
):


    serializer_class = CommentSerializer



    permission_classes = [

        IsAuthenticatedOrReadOnly,

    ]








    def get_queryset(self):


        queryset = (

            Comment.objects

            .select_related(

                "user",

                "post",

            )

        )



        user = self.request.user



        if (

            user.is_authenticated

            and user.is_superuser

        ):

            return queryset





        return queryset.filter(

            is_approved=True

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









    @action(

        detail=True,

        methods=[

            "post"

        ],

        permission_classes=[

            IsSuperUser

        ],

    )

    def approve(

        self,

        request,

        pk=None,

    ):


        comment = self.get_object()



        comment = approve_comment(

            comment

        )



        serializer = self.get_serializer(

            comment

        )



        return Response(

            serializer.data

        )
