from django.urls import path
from .views import UserProfileModelGenericAPIView, UserPostListGenericAPIView,UserProfileDisplayCurrentUserDetailGenericAPIView

urlpatterns = [
    path("create-user/", UserProfileModelGenericAPIView.as_view(), name="UserProfileModelGenericAPIView"),
    path("view-posts/", UserPostListGenericAPIView.as_view(), name="UserPostListAPIView"),
    path("view-profile/", UserProfileDisplayCurrentUserDetailGenericAPIView.as_view(), name="UserProfileDisplayCurrentUserDetailGenericAPIView")
]
