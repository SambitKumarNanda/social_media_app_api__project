from django.shortcuts import render
from api.get_country import get_countries
from django.http import response


# Create your views here.

def showView(request):
    country_names = get_countries().json()
    for country_name in country_names:
        print(country_name['country_name'])
    return response.HttpResponse(country_names)
