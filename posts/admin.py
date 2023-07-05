from django.contrib import admin
from .models import UserPostModel, PostCommentModel
# Register your models here.
admin.site.register(UserPostModel)
admin.site.register(PostCommentModel)