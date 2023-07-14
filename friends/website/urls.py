from django.urls import path
from .views import FriendRequestModelSendRequestAPIView, FriendRequestModelAcceptAPIView

urlpatterns = [
    path("send-request/<id>", FriendRequestModelSendRequestAPIView.as_view(), name="FriendRequestModelSendRequestGenericAPIView"),
    path("accept-request/<id>", FriendRequestModelAcceptAPIView.as_view(), name="FriendRequestModelAcceptAPIView")
]