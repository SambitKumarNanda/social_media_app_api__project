from .serializer import FriendModelSerializerSendRequestSerializer
from ..models import FriendModel
from rest_framework import generics, status
from rest_framework.response import Response


class FriendRequestModelSendRequestGenericAPIView(generics.GenericAPIView):
    queryset = FriendModel.objects.all()
    serializer_class = FriendModelSerializerSendRequestSerializer
    #
    # def post(self, request, id):
    #
    #     return d
