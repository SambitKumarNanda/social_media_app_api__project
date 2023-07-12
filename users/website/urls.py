from django.urls import path
from .views import WebsiteRegisterGenericAPIView, WebsiteCreateOTPView, WebsiteVerifyUserLogin

urlpatterns = [
    path("register-user/", WebsiteRegisterGenericAPIView.as_view(), name="WebsiteRegisterGenericAPIView"),
    path("generate-otp/", WebsiteCreateOTPView.as_view(), name="WebsiteCreateOTPView"),
    path("verify-otp-login/", WebsiteVerifyUserLogin.as_view(), name="WebsiteVerifyUserLogin"),
]
