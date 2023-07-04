from django.urls import path, include

urlpatterns = [
    path("website/api/", include('userprofile.website.urls')),
    path("app/api/", include('userprofile.app.urls')),
    path("dashboard/api/", include('userprofile.dashboard.urls'))
]
