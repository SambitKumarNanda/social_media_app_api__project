from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices


# Create your models here.
class FriendModel(models.Model):
    friends = models.ManyToManyField(get_user_model(), related_name="UserProfileModel_friends", blank=True)
    friend_req_receieved = models.ManyToManyField(get_user_model(),
                                                  related_name="UserProfileModel_friend_req_receieved", blank=True)
    REQUEST_STATUS = Choices('ACCEPTED', 'PENDING', 'REJECTED')
    friend_req_sent = models.ManyToManyField(get_user_model(), related_name="UserProfileModel_friend_req_sent",
                                             blank=True)
