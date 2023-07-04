from django.urls import path
from .views import WebsiteRegisterGenericAPIView

urlpatterns = [
    path("register-user/", WebsiteRegisterGenericAPIView.as_view(), name="WebsiteRegisterGenericAPIView")
]
