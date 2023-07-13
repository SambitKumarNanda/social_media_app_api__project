from django.urls import path
from .views import FriendRequestModelSendRequestAPIView

urlpatterns = [
    path("send-request/<id>", FriendRequestModelSendRequestAPIView.as_view(), name="FriendRequestModelSendRequestGenericAPIView"),
    # path("accept-request", FriendRequestModelAcceptRequestGenericAPIView.as_view(), name="FriendRequestModelAcceptRequestGenericAPIView")
]