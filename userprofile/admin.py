from django.contrib import admin
from .models import UserAddressModel, UserEducationModel, UserContactDetailModel, UserProfileModel
# Register your models here.
admin.site.register(UserAddressModel)
admin.site.register(UserEducationModel)
admin.site.register(UserProfileModel)
admin.site.register(UserContactDetailModel)