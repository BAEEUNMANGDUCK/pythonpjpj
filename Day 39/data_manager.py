import requests

SHEETY_URL = "https://api.sheety.co/d8b4d640fe785403eef0cbdd3772a1de/myFlightDeals/prices"
headers ={
    "Content-Type": "application/json"
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, sheet_data: list[dict]):
        self.sheet_data = sheet_data
        print(self.sheet_data)
    def send_to_google_sheet(self):
        for each_data in self.sheet_data:
            update_data = {
                #### 주의 #### 이름이 완전 똑같아야 함. ex) 'iataCode': ~~['iataCode'], 딕셔너리 안에 딕셔너리로 또 감싸는 것도 잊지 말아야 함
                "price": {
                          'iataCode': each_data['iataCode'],
                          }
            }
            print(each_data['iataCode'])
            response = requests.put(url=f"{SHEETY_URL}/{each_data['id']}", json=update_data)
            print(response.text)
