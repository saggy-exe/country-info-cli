import requests
from config import BASE_URL

def get_country(name):
    url = f"{BASE_URL}{name}"
    params = {
        "fullText": "true",
        "fields": "name,capital,population,region,languages,currencies,flag"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Country not found or API error")

    return response.json()[0]