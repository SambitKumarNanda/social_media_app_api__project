from django.contrib import admin
from .models import AdvertisementsModel, AdvertisementBannerModel

# Register your models here.
admin.site.register(AdvertisementsModel)
admin.site.register(AdvertisementBannerModel)