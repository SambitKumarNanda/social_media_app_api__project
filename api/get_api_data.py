import requests

API_TOKEN = "EYhGKU03tD2RqgEuZU9RNpPoTHy4Kgo0yOWl_fPciEpythi2FBVfQHqDsQ5o44GaVDc"
USER_EMAIL = "nanu2647542@gmail.com"


def get_access_token():
    url = "https://www.universal-tutorial.com/api/getaccesstoken"
    r = requests.get(url,
                     headers={'Content-Type': 'application/json', 'Accept': 'appplication/json', 'api-token': API_TOKEN,
                              'user-email': USER_EMAIL})
    # print(r.json()["auth_token"])
    return r


def get_countries():
    url = "https://www.universal-tutorial.com/api/countries/"
    req = requests.get(url, headers={'Authorization': f"Bearer {get_access_token().json()['auth_token']}", 'Accept': 'application/json', })

    return req


def get_states():
    url = "http://www.universal-tutorial.com/api/states/{country_name}"
    req = requests.get(url, headers={'Authorization': f"Bearer {get_access_token().json()['auth_token']}", 'Accept':'application/json'})
    return req