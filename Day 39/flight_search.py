import requests
import os
from dotenv import load_dotenv
load_dotenv()
TEQUILA_URL = "https://api.tequila.kiwi.com/locations/query"
API_KEY = os.environ.get("API_KEY")



class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, city: dict):
        self.city = city
        # print(self.city)

    def get_update_data(self) -> dict:
        params = {
            "term": self.city['city'],
            "locale": "en-US",
            "location_types": "airport",
        }
        headers = {
            "apikey": API_KEY
        }
        search_iata = requests.get(url=TEQUILA_URL, params=params, headers=headers).json()
        # print(search_iata)
        self.city['iataCode'] = search_iata["locations"][0]['id']
        return self.city
