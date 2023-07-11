from django.urls import path
from .views import showAllDataView, populateCountryView, populateStateView, populateCityView

urlpatterns = [
    path("showapidata/", showAllDataView, name="showallDataView"),
    path("populatecountry/", populateCountryView, name="populatecountry"),
    path("populatestate/", populateStateView, name="populatestate"),
    path("populatecity/", populateCityView, name="populatecity"),
]
