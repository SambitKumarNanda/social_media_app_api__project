from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import MessageModelSerializer, MessageModelListSerializer
from django.contrib.auth import get_user_model
from ..models import MessageModel


class MessageModelCreateGenericAPIView(generics.GenericAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer

    def post(self, request):
        serializer = MessageModelSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "message sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error_message": "Error message"}, status=status.HTTP_400_BAD_REQUEST)


class MessageModelListGenericAPIView(generics.ListAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelListSerializer
