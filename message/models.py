from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class MessageModel(models.Model):
    message = models.CharField(max_length=100)
    receiver_addr = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                      related_name="MessageModel_receiver_addr", null=True, blank=True)
    sender_addr = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
