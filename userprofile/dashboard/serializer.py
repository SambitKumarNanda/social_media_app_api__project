from rest_framework import serializers
from ..models import UserProfileModel, UserEducationModel, UserContactDetailModel, UserAddressModel
from posts.website.serializer import UserPostListSerializer


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
    education_addr = serializers.SerializerMethodField()
    contact_no = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileModel
        fields = "__all__"

    def get_education_addr(self, obj):
        try:
            data = UserEducationModelSerializer(obj.education_addr.all(), many=True).data
        except:
            data = []
        return data

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

    def get_posts(self, obj):
        try:
            data = UserPostListSerializer(obj.posts.all(), many=True).data
        except:
            data=[]
        return data

