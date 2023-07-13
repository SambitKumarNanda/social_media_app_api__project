from django.contrib import admin
from .models import FriendModel, FriendRequestModel, FriendRequestSentModel
# Register your models here.
admin.site.register(FriendModel)
admin.site.register(FriendRequestModel)
admin.site.register(FriendRequestSentModel)
