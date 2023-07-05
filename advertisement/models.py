from django.db import models


# Create your models here.
class AdvertisementBannerModel(models.Model):
    media = models.FileField(upload_to="advertisment-media/")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AdvertisementsModel(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ManyToManyField(AdvertisementBannerModel, related_name="AdvertismentsModel_banner", blank=True)
    redirection_link = models.URLField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
