from django.contrib.auth import get_user_model
from rest_framework import serializers
from userprofile.models import UserProfileModel


class WebsiteRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        UserProfileModel.objects.create(user=user)
        return validated_data
