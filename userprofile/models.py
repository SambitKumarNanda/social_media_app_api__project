from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from posts.models import UserPostModel
from friends.models import FriendModel, FriendRequestModel, FriendRequestSentModel
from coreUtils.models import CountryModel, StateModel, CityModel, PrimaryEducationAddressModel, \
    SecondaryEducationAddressModel, HigherEducationAddressModel, CollegeEducationModel, EmploymentModel


# Create your models here.

class UserContactDetailModel(models.Model):
    mobile_no1 = models.IntegerField(null=True, blank=True, unique=True)
    mobile_no2 = models.IntegerField(null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mobile_no1)


class UserAddressModel(models.Model):
    address1 = models.TextField(max_length=100, null=True, blank=True)
    address2 = models.TextField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name="UserAddressModel_country",
                                null=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="UserAddressModel_state",
                              null=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="UserAddressModel_city",
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address1


class UserEducationModel(models.Model):
    primay_edu = models.ForeignKey(PrimaryEducationAddressModel, on_delete=models.CASCADE,
                                   related_name="UserEducationModel_primary_edu", blank=True, null=True)
    secondary_edu = models.ForeignKey(SecondaryEducationAddressModel, on_delete=models.CASCADE,
                                      related_name="UserEducationModel_secondary_edu", blank=True, null=True)
    higher_edu = models.ForeignKey(HigherEducationAddressModel, on_delete=models.CASCADE,
                                   related_name="UserEducationModel_higer_edu", blank=True, null=True)
    college_edu = models.ForeignKey(CollegeEducationModel, on_delete=models.CASCADE,
                                    related_name="UserEducationModel_college_edu", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(
    ), on_delete=models.CASCADE, related_name="UserProfileModel_user")
    GENDER = Choices(('M', 'MALE'), ('F', 'FEMALE'))
    gender = models.CharField(max_length=1, choices=GENDER)
    user_profile_pic = models.FileField(
        upload_to="profile-image/", null=True, blank=True)
    user_profile_bg_pic = models.FileField(
        upload_to="profile-bg-image/", null=True, blank=True)
    user_bio = models.CharField(max_length=100, null=True, blank=True)
    contact_no = models.ManyToManyField(
        UserContactDetailModel, blank=True, related_name="UserProfileModel_contact_no")

    # Address Information
    address = models.ManyToManyField(
        UserAddressModel, blank=True, related_name="UserProfileModel_address")
    education_addr = models.ForeignKey(
        UserEducationModel, on_delete=models.CASCADE, null=True, related_name="UserProfileModel_education_addr")
    workplace_addr = models.ForeignKey(EmploymentModel, on_delete=models.CASCADE, blank=True,
                                       related_name="UserProfileModel_workplace_addr", null=True)

    # Post Info About the UserProfile
    posts = models.ManyToManyField(UserPostModel, blank=True)

    # Friend Information
    friends = models.ManyToManyField(
        FriendModel, blank=True, related_name="UserProfileModel_friend")
    friend_reqests_sent = models.ManyToManyField(
        FriendRequestSentModel, blank=True, related_name="UserProfileModel_friend_reqests_sent")
    friend_reqests_recieved = models.ManyToManyField(
        FriendRequestModel, blank=True, related_name="UserProfileModel_friend_reqests_received")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
