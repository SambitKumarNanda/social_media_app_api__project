from rest_framework import serializers
from ..models import UserPostModel, PostCommentModel
from userprofile.models import UserProfileModel


class UserPostModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostModel
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        userprofile_instance = UserProfileModel.objects.get(user=self.context['request'].user)
        print(userprofile_instance.posts)
        post_title = validated_data.pop('post_title')
        post_image = validated_data.pop('post_image')
        posts = UserPostModel.objects.create(
            post_title=post_title,
            post_image=post_image,
        )
        print(post_title)
        print(post_image)
        userprofile_instance.posts.create(
            post_title=post_title,
            post_image=post_image,
        )
        return validated_data


class UserPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostModel
        fields = "__all__"


class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCommentModel
        fields = "__all__"

    def create(self, validated_data):
        comment_instance = PostCommentModel.objects.create(**validated_data)
        post_instance = UserPostModel.objects.get(id=self.context['id'])
        post_instance.comments.add(comment_instance)
        post_instance.save()
        return validated_data
