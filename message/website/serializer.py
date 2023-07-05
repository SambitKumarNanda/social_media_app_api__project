from rest_framework import serializers
from ..models import MessageModel


class MessageModelSerializer(serializers.ModelSerializer):

    # receiver_addr = serializers.ChoiceField(choices=users.objects.all())

    class Meta:
        model = MessageModel
        fields = ['id', 'message', 'receiver_addr']

    def create(self, validated_data):
        receiver_addr = validated_data.get('receiver_addr')
        message = validated_data.get('message')
        msgmodel = MessageModel.objects.create(message=message, sender_addr=self.context['request'].user,
                                               receiver_addr=receiver_addr)
        return msgmodel

    # def get_filtered_receiver_addr(self, obj):
    #     current_user = self.context['request'].user
    #     return [user for user in obj.receiver_addr if user != current_user]


class MessageModelListSerializer(serializers.ModelSerializer):
    receiver_addr_detail = serializers.SerializerMethodField()
    sender_addr_detail = serializers.SerializerMethodField()

    class Meta:
        model = MessageModel
        fields = "__all__"

    def get_receiver_addr_detail(self, obj):
        try:
            data = obj.receiver_addr.username
        except:
            data = []
        return data

    def get_sender_addr_detail(self, instance):
        try:
            data = instance.sender_addr.username
        except:
            data = []
        return data
