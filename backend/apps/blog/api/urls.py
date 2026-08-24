from rest_framework.routers import DefaultRouter


from apps.blog.views import (
    PostViewSet,
)


from apps.blog.comment_views import (
    CommentViewSet,
)





router = DefaultRouter()



router.register(
    "posts",
    PostViewSet,
    basename="posts",
)



router.register(
    "comments",
    CommentViewSet,
    basename="comments",
)




urlpatterns = router.urls
