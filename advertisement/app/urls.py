from django.urls import path
from .views import AdvertisementModelListAPIView

urlpatterns = [
    path("banner-list-api/", AdvertisementModelListAPIView.as_view(), name="AdvertisementModelList")
]