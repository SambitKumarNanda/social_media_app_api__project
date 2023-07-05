from django.urls import path
from .views import MessageModelCreateGenericAPIView, MessageModelListGenericAPIView, MessageModelListMessageFilter
urlpatterns=[
    path("send-message/", MessageModelCreateGenericAPIView.as_view(), name="MessageModelCreateGenericAPIView"),
    path("show-messages/", MessageModelListGenericAPIView.as_view(), name="MessageModelListGenericAPIView"),
    path("filter-message/", MessageModelListMessageFilter.as_view(), name="MessageModelListMessageFilter"),
]