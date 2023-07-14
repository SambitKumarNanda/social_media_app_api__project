from rest_framework import serializers
from ..models import UserProfileModel, UserEducationModel, UserContactDetailModel, UserAddressModel
# from friends.website.serializer import FriendModelListSerializer


class UserEducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEducationModel
        fields = "__all__"


class UserPhoneNumberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactDetailModel
        fields = "__all__"


class UserAddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddressModel
        fields = "__all__"


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["gender", "user_profile_pic", "user_profile_bg_pic", "user_bio", "contact_no", "address",
                  "education_addr", "workplace_addr", "posts", "friends"]


class UserProfileModelListSerializer(serializers.ModelSerializer):
    contact_no = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    education_addr = serializers.SerializerMethodField()
    # friends = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileModel
        fields = '__all__'

    def get_contact_no(self, obj):
        try:
            data = UserPhoneNumberModelSerializer(obj.contact_no.all(), many=True).data
        except:
            data = []
        return data

    def get_address(self, obj):
        try:
            data = UserAddressModelSerializer(obj.address.all(), many=True).data
        except:
            data = []
        return data

    def get_education_addr(self, obj):
        try:     
            data = UserPhoneNumberModelSerializer(obj.education_addr.all(), many=True).data
        except:
            data = []
        return data

    # def get_friends(self, obj):
    #     try:
    #         data = FriendModelListSerializer(obj.friends.all(), many=True).data
    #     except:
    #         data = []
    #     return data
