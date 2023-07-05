from .serializer import FriendModelSerializerSendRequestSerializer, FriendModelListSerializer
from ..models import FriendModel
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import FriendModelAcceptSerializer


class FriendRequestModelSendRequestGenericAPIView(generics.GenericAPIView):
    queryset = FriendModel.objects.all()
    serializer_class = FriendModelSerializerSendRequestSerializer

    def post(self, request):
        serializer = FriendModelSerializerSendRequestSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Friend request has been sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Error has been found at, {serializer.errors}"},
                            status=status.HTTP_400_BAD_REQUEST)


class FriendRequestModelAcceptRequestGenericAPIView(generics.GenericAPIView):
    queryset = FriendModel.objects.all()
    serializer_class = FriendModelListSerializer

    def put(self, request, id):
        query = FriendModel.objects.all()
        serializer = FriendModelAcceptSerializer(data=query, instance=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Friend Request has been accepted"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Error has been found at, {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
