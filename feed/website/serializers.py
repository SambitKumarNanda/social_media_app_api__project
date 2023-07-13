from rest_framework import serializers
from ..models import FeedModel


class FeedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedModel
        fields = ["advertisement", "posts"]

