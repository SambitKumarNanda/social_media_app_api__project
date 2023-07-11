from django.urls import path
from .views import populateCountryView

urlpatterns = [
    path("populatecountry/", populateCountryView, name="populatecountry"),
]
