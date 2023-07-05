from django.db import models
# from userprofile.models import UserProfileModel
from django.contrib.auth import get_user_model


# Create your models here.

class PostCommentModel(models.Model):
    comment = models.CharField(max_length=100, null=True, blank=True)
    userprofile = models.ForeignKey(get_user_model(), blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserPostModel(models.Model):
    post_title = models.CharField(max_length=100)
    post_image = models.FileField(upload_to='posts/post-image/', null=True, blank=True)
    likes = models.ManyToManyField(get_user_model(), blank=True)
    comments = models.ManyToManyField(PostCommentModel, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title
