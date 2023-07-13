from django.db import models
from advertisement.models import AdvertisementsModel
from posts.models import UserPostModel

# Create your models here.
class FeedModel(models.Model):
    advertisement = models.ManyToManyField(AdvertisementsModel, blank=True, related_name="FeedModel_advertisement")
    posts = models.ManyToManyField(UserPostModel, blank=True, related_name="FeedModel_posts")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)