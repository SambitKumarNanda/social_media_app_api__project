from .views import FeedModelDisplayGenericAPIView
from django.urls import path

urlpatterns = [
    path("show-feed/", FeedModelDisplayGenericAPIView.as_view(), name="FeedModelDisplayGenericAPIView"),
]
