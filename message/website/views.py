from rest_framework import generics, status, filters
from rest_framework.response import Response
from .serializer import MessageModelSerializer, MessageModelListSerializer
from django.contrib.auth import get_user_model
from ..models import MessageModel
from django_filters.rest_framework import DjangoFilterBackend


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


class MessageModelListMessageFilter(generics.ListAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["receiver_addr", 'sender_addr']
    ordering_fields = ["created_at"]

    def get_queryset(self):
        user_instance = self.request.user
        queryset = MessageModel.objects.filter(sender_addr=user_instance)
        return queryset

    def get(self, request):
        serializer = MessageModelSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
