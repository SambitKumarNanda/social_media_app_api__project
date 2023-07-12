from django.contrib.auth import get_user_model
from rest_framework import serializers
from userprofile.models import UserProfileModel
from ..models import OTPModel

class WebsiteRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email","password","username"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        UserProfileModel.objects.create(user=user)
        return validated_data


class WebsiteVerifyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OTPModel
        fields = ["email","code"]
        
    def validate(self, data):
        email_instance = data['email']
        otp_instance = data['code']
        
        print(data,1)
        
        if OTPModel.objects.filter(email=email_instance, code=otp_instance,is_active=True).exists():
            return data
        else:
            raise serializers.ValidationError("The data you have entered seems to be incorrect")