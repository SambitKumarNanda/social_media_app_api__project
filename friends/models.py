from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices


# Create your models here.
class FriendModel(models.Model):
    friends = models.ManyToManyField(get_user_model(), blank=True, related_name="FriendModel_friends")
    request_status = models.CharField(max_length=10, blank=True, null=True, default="ACCEPTED")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FriendRequestModel(models.Model):
    requested_user = models.ManyToManyField(get_user_model(), blank=True, related_name="FriendRequestModel_sender")
    request_status = models.CharField(max_length=10, blank=True, null=True, default="PENDING")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FriendRequestSentModel(models.Model):
    sender =  models.ManyToManyField(get_user_model(), blank=True, related_name="FriendRequestSentModel")
    request_status = models.CharField(max_length=10, blank=True, null=True, default="PENDING")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)