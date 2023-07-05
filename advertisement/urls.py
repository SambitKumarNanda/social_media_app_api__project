from django.urls import path

from django.urls import path,include

urlpatterns = [
    path("app/api/", include('advertisements.app.urls')),
    path("website/api/", include("advertisements.website.urls")),
    path("dashboard/api/", include("advertisements.dashboard.urls"))
]