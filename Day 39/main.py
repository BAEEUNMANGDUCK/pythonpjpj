# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv
load_dotenv()

SHEETY_URL = os.environ.get('SHEETY_URL')

# TODO 1 구글 시트에서 데이터 가지고 오고 iata code 값 바꾸기
sheet_data = requests.get(url=SHEETY_URL).json()['prices']

need_update = False
update_datas = []
for city in sheet_data:
    if len(city['iataCode']) == 0:
        flight_search = FlightSearch(city=city)
        updated = flight_search.get_update_data()
        update_datas.append(updated)
        need_update = True

# # # TODO 2 update_datas 를 dataManager 객체의 인자로 보내서 구글시트에 업데이트 시킨다.

if need_update:
    dataManager = DataManager(update_datas)
    dataManager.send_to_google_sheet()
else:
    update_datas = sheet_data

# TODO 3 항공권을 검색하기 위해 FlightData 클래스의 객체 생성
ticket_data = []
for city in update_datas:
    flightData = FlightData(city=city)
    ticket_data.append(flightData.search_ticket())


# TODO 4 구글 시트에 작성된 가격보다 싸면 SMS 메세지 발송

for ticket_info, update_data in zip(ticket_data, update_datas):
    notificationManager = NotificationManager(ticket_info, update_data)
    notificationManager.send_message()
