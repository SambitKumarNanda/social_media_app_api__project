from django.contrib import admin
from .models import UserModel, OTPModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(OTPModel)