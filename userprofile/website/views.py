from ..models import UserProfileModel
from .serializer import UserProfileModelSerializer, UserProfileModelListSerializer
from posts.website.serializer import UserPostListSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from posts.models import UserPostModel


class UserProfileModelGenericAPIView(generics.GenericAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileModelSerializer

    def put(self, request):
        query = UserProfileModel.objects.get(user=request.user)
        serializer = UserProfileModelSerializer(instance=query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User successfully created"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDisplayCurrentUserDetailGenericAPIView(generics.GenericAPIView):
    queryset = UserPostModel.objects.all()
    serializer_class = UserProfileModelListSerializer

    def get(self, request):
        try:
            user_instance = request.user
            query_set = UserProfileModel.objects.get(user=user_instance)
            serializer = UserProfileModelListSerializer(query_set, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Error has occured, {e}"}, status=status.HTTP_200_OK)


class UserPostListAPIView(generics.GenericAPIView):
    queryset = UserPostModel.objects.all()
    serializer_class = UserProfileModelSerializer

    def get(self, request):
        try:
            current_user_instance = request.user
            queryset = UserProfileModel.objects.get(user=current_user_instance).posts.all()
            serializer = UserPostListSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": f"Error has occurred, {e}"}, status=status.HTTP_400_BAD_REQUEST)

