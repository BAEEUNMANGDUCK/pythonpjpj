import os
import requests
# pip install twilio가 잘 안되는 경우가 있는데 경로 이름이 너무 길어서이다. 오류 링크가 하라는 방법대로 레지스트리 에디터 연 다음 해당 값을 1로 바꿔주면 됨. 
from twilio.rest import Client

# Call 5 day / 3 hour weather forecast data
API_KEY= "blahblah"
MY_URL = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 51.507351
MY_LNG = -0.127758

# # Twilio
account_sid = "blahblah"
auth_token = "blahblah"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY
}

response = requests.get(url=MY_URL, params=parameters)
response.raise_for_status()
datas = response.json()['list']
weather_datas = [data['weather'][0]['id'] for data in datas[:6]]
print(weather_datas)
for weather_code in weather_datas:
    if weather_code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                    body ="bring an Umbrella",
                    from_="blahblah",
                    to="blahblah"
                )
        print(message.status)
        break
   


