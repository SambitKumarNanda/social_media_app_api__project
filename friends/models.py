from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices


# Create your models here.
class FriendModel(models.Model):
    friends = models.ForeignKey(get_user_model(), null=True, related_name="FriendModel_friends", on_delete=models.CASCADE)
    request_status = models.CharField(max_length=10, blank=True, null=True, default="ACCEPTED")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.friends.email
    

class FriendRequestModel(models.Model):
    requested_user = models.ForeignKey(get_user_model(), null=True, related_name="FriendRequestModel_sender", on_delete=models.CASCADE)
    request_status = models.CharField(max_length=10, blank=True, null=True, default="PENDING")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.requested_user.email
    
    
class FriendRequestSentModel(models.Model):
    sent_to =  models.ForeignKey(get_user_model(), null=True, related_name="FriendRequestSentModel_sent_to", on_delete=models.CASCADE)
    request_status = models.CharField(max_length=10, blank=True, null=True, default="PENDING")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def ___str__(self):
        return self.sent_to.email