from .serializers import AdvertisementBannerSerializer, AdvertisementModelSerializer
from ..models import AdvertisementBannerModel, AdvertisementsModel
from rest_framework import generics, status
from rest_framework.response import Response


class AdvertisementModelListAPIView(generics.ListAPIView):
    queryset = AdvertisementsModel.objects.all()
    serializer_class = AdvertisementModelSerializer
