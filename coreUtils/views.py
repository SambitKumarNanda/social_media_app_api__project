from django.shortcuts import render
from .models import CountryModel
from django.http import response
from api.get_api_data import get_countries


# Create your views here.

def populateCountryView(request):
    country_list = get_countries().json()
    for country in country_list:
        CountryModel.objects.create(
            title=country['country_name']
        )
        print(country['country_name'])
    return response.HttpResponse("Database Populated")


def populateStateView(request):
    country_list = get_countries().json()
