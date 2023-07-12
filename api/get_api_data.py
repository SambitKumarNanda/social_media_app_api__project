import requests

API_TOKEN = "EYhGKU03tD2RqgEuZU9RNpPoTHy4Kgo0yOWl_fPciEpythi2FBVfQHqDsQ5o44GaVDc"
USER_EMAIL = "nanu2647542@gmail.com"


def get_access_token():
    url = "https://www.universal-tutorial.com/api/getaccesstoken"
    return requests.get(url,
                        headers={'Content-Type': 'application/json', 'Accept': 'appplication/json', 'api-token': API_TOKEN,
                                 'user-email': USER_EMAIL})


AUTH_TOKEN = get_access_token().json()['auth_token']
# print(AUTH_TOKEN)


def get_countries():
    url = "https://www.universal-tutorial.com/api/countries/"
    return requests.get(url, headers={'Authorization': f"Bearer {AUTH_TOKEN}", 'Accept': 'application/json', })


def get_states(country_name):
    url = f"http://www.universal-tutorial.com/api/states/{country_name}"
    return requests.get(url, headers={'Authorization': f"Bearer {AUTH_TOKEN}", 'Accept': 'application/json'})


def get_cities(state_name):
    url = f"https://www.universal-tutorial.com/api/cities/{state_name}"
    return requests.get(url, headers={'Authorization': f"Bearer {AUTH_TOKEN}", 'Accept': 'application/json'})
