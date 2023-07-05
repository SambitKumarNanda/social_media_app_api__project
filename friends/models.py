from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices


# Create your models here.
class FriendModel(models.Model):
    REQUEST_STATUS = Choices(('ACCEPTED', 'ACCEPTED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'))
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS, default=REQUEST_STATUS.PENDING)
    target_user = models.ManyToManyField(get_user_model(), blank=True, related_name="FriendModel_target_user")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
