from django.urls import path, include

urlpatterns = [
    path("website/api/", include('message.website.urls'))
]