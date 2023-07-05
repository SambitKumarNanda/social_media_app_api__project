from .serializers import AdvertisementBannerSerializer, AdvertisementModelSerializer
from ..models import AdvertisementBannerModel, AdvertisementsModel
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class AdvertisementBannerModelCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = AdvertisementBannerModel.objects.all()
    serializer_class = AdvertisementBannerSerializer


class AdvertisementModelCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = AdvertisementsModel.objects.all()
    serializer_class = AdvertisementModelSerializer
