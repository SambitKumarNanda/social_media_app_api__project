from django.shortcuts import render
from .models import CountryModel, StateModel, CityModel
from django.http import response
from api.get_api_data import get_countries, get_states, get_cities


# Create your views here.

def showAllDataView(request):
    country_names = get_countries().json()
    for country_name in country_names:
        print(country_name['country_name'])
    return response.HttpResponse(country_names)


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
    for country in country_list:
        # print(country['country_name'])
        state_list = get_states(country['country_name'])
        try:
            for state in state_list.json():
                StateModel.objects.create(
                    title=state['state_name'],
                    country=CountryModel.objects.get(title=country['country_name'])
                )
                print("Added to database")
        except Exception:
            print('No data')
    return response.HttpResponse("data fetched successfully")


def populateCityView(request):
    query_state_list = StateModel.objects.filter(country=CountryModel.objects.get(title='India'))
    for state in query_state_list:
        try:
            for city in get_cities(state).json():
                CityModel.objects.create(
                    title=city['city_name'],
                    country=CountryModel.objects.get(title='India'),
                    state=state,
                )
                print('Added to db')
        except Exception:
            print('No data')
    return response.HttpResponse("data fetched successfully")
