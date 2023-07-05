from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from posts.models import UserPostModel
from friends.models import FriendModel


# Create your models here.

class UserPhoneNumberModel(models.Model):
    mobile_no = models.IntegerField(null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mobile_no)


class UserAddressModel(models.Model):
    address = models.TextField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserEducationModel(models.Model):
    edu_address = models.TextField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="UserProfileModel_user")
    GENDER = Choices(('M', 'MALE'), ('F', 'FEMALE'))
    gender = models.CharField(max_length=1, choices=GENDER)
    user_profile_pic = models.FileField(upload_to="profile-image/", null=True, blank=True)
    user_profile_bg_pic = models.FileField(upload_to="profile-bg-image/", null=True, blank=True)
    user_bio = models.CharField(max_length=100, null=True, blank=True)
    contact_no = models.ManyToManyField(UserPhoneNumberModel, blank=True, related_name="UserProfileModel_contact_no")
    address = models.ManyToManyField(UserAddressModel, blank=True, related_name="UserProfileModel_address")
    education_addr = models.ManyToManyField(UserEducationModel, blank=True)
    posts = models.ManyToManyField(UserPostModel, blank=True)
    friends = models.ManyToManyField(FriendModel, blank=True, related_name="UserProfileModel_friend")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
