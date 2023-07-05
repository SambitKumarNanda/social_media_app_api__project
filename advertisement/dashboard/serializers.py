from rest_framework import serializers
from ..models import AdvertisementBannerModel, AdvertisementsModel


class AdvertisementBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementBannerModel
        fields = "__all__"


class AdvertisementModelSerializer(serializers.ModelSerializer):
    banner = serializers.SerializerMethodField()

    class Meta:
        model = AdvertisementsModel
        fields = "__all__"

    def get_banner(self, obj):
        try:
            data = AdvertisementBannerSerializer(obj.banner.all(), many=True).data
        except:
            data = []
        return data