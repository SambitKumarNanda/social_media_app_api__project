from django.urls import path, include
urlpatterns = [
    path("website/api/", include('posts.website.urls')),
    path("app/api/", include('posts.app.urls'))
]