from rest_framework import status, generics
from rest_framework.response import Response
from .serializer import UserProfileModelSerializer
from ..models import UserProfileModel


class UserProfileModelListViewAPI(generics.ListAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileModelSerializer
