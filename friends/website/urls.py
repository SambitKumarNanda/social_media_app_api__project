from django.urls import path
from .views import FriendRequestModelSendRequestGenericAPIView, FriendRequestModelAcceptRequestGenericAPIView

urlpatterns = [
    path("send-request/", FriendRequestModelSendRequestGenericAPIView.as_view(), name="FriendRequestModelSendRequestGenericAPIView"),
    path("accept-request", FriendRequestModelAcceptRequestGenericAPIView.as_view(), name="FriendRequestModelAcceptRequestGenericAPIView")
]