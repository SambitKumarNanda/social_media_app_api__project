from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import UserPostModelCreateSerializer, PostCommentCreateSerializer
from ..models import UserPostModel, PostCommentModel


class UserPostModelCreateAPIView(generics.GenericAPIView):
    queryset = UserPostModel.objects.all()
    serializer_class = UserPostModelCreateSerializer

    def post(self, request):
        serializer = UserPostModelCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Post successfully uploaded"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PostCommentModelCreateAPIView(generics.GenericAPIView):
    queryset = PostCommentModel.objects.all()
    serializer_class = PostCommentCreateSerializer

    def put(self, request, id):
        try:
            query = UserPostModel.objects.get(id=id)
            serializer = UserPostModelCreateSerializer(data=request.data, instance=query)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "data saved successfully"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
