from django.contrib import admin
from .models import AdvertismentsModel, AdvertismentBannerModel

# Register your models here.
admin.site.register(AdvertismentsModel)
admin.site.register(AdvertismentBannerModel)