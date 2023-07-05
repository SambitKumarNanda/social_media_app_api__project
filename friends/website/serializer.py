from rest_framework import serializers
from ..models import FriendModel


class FriendModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendModel
        fields = "__all__"
