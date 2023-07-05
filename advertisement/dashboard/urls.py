from django.urls import path
from .views import AdvertisementBannerModelCreateAPIView, AdvertisementModelCreateAPIView

urlpatterns = [
    path("banner-create-api/", AdvertisementBannerModelCreateAPIView.as_view(), name="AdvertisementBannerModelCreateAPIView"),
    path("advertisement-create-api/", AdvertisementModelCreateAPIView.as_view(), name="AdvertisementModelCreateAPIView")
]