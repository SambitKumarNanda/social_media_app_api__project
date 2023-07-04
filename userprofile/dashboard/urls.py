from .views import UserProfileModelListViewAPI
from django.urls import path

urlpatterns=[
    path("show-user/", UserProfileModelListViewAPI.as_view(), name="UserProfileModelListViewAPI")
]