import requests
from pprint import pprint
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

TICKET_URL = "https://api.tequila.kiwi.com/search"
API_KEY = os.environ.get('API_KEY')

# 내일부터 6달 후까지 검색
now = datetime.now()
date_from = (now + timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (now + timedelta(days=180)).strftime("%d/%m/%Y")

# 최소 체류, 최대 체류 기간
NIGHTS_FROM = 7
NIGHTS_TO = 28

# 출발지
FLY_FROM = "LON"

# 통화
CURR = "GBP"


class FlightData:

    def __init__(self, city):
        self.city = city
        # print(self.city)

    def search_ticket(self):
        headers = {
            "apikey": API_KEY
        }

        params = {
            "fly_from": FLY_FROM,
            "fly_to": self.city['iataCode'],
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": CURR
        }

        response = requests.get(url=TICKET_URL, params=params, headers=headers)
        try:
            data = response.json()['data'][0]
            # print(data)
            price = data['price']
            city_from = data['cityFrom']
            fly_from = data['flyFrom']
            city_to = data['cityTo']
            fly_to = data['flyTo']
            arrival = datetime.fromtimestamp(int(data['aTime']))
            comeback = arrival + timedelta(days=data['nightsInDest'])

            return [price, city_from, fly_from, city_to, fly_to, arrival.strftime("%Y-%m-%d"), comeback.strftime("%Y-%m-%d")]
        except IndexError:
            return None
