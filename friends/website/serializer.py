from rest_framework import serializers
from ..models import FriendModel


class FriendModelSerializerSendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendModel
        fields = ["id"]


class FriendModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendModel
        fields = "__all__"


class FriendModelAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendModel
        fields = ['target_user']
