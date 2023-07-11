from django.urls import path
from django.urls import path,include

urlpatterns = [
    path("app/api/", include('advertisement.app.urls')),
    path("website/api/", include("advertisement.website.urls")),
    path("dashboard/api/", include("advertisement.dashboard.urls")),
]