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
