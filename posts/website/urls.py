from django.urls import path
from .views import UserPostModelCreateAPIView, PostCommentModelCreateAPIView

urlpatterns = [
    path("create-post/", UserPostModelCreateAPIView.as_view(), name="UserPostModelCreateAPIView"),
    path("post-comment/<id>/", PostCommentModelCreateAPIView.as_view(), name="PostCommentModelCreateAPIView")
]
