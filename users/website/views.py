from .serializers import WebsiteRegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response


class WebsiteRegisterGenericAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = WebsiteRegisterSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
