from django.urls import path
from .views import UserProfileModelGenericAPIView, UserPostListAPIView,UserProfileDisplayCurrentUserDetailGenericAPIView

urlpatterns = [
    path("create-user/", UserProfileModelGenericAPIView.as_view(), name="UserProfileModelGenericAPIView"),
    path("view-posts/", UserPostListAPIView.as_view(), name="UserPostListAPIView"),
    path("view-profile/", UserProfileDisplayCurrentUserDetailGenericAPIView.as_view(), name="UserProfileDisplayCurrentUserDetailGenericAPIView")
]
