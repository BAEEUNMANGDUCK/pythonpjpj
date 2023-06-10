import requests
import os
from twilio.rest import Client

api_key = "{my api_key}"
account_sid = "{my account_sid}"
auth_token = "{my auth_token}"
seoul_lat = 37.5683
seoul_lon = 126.9778

weather_params = {
    "lat": seoul_lat,
    "lon": seoul_lon,
    "appid": api_key
}

weather_endpoints = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=weather_endpoints, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['list'][:5]
# for per_three in range(5):
#     weather_id = weather_data['list'][per_three]['weather'][0]['id']
#     if weather_id < 700:
#         print(weather_data['list'][per_three]['weather'][0]['id'])
#         print("Bring a umbrella")
#         break
# twilio
for weather in weather_slice:
    if weather['weather'][0]['id'] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Today it will rain, Please Bring an umbrella",
            from_='{phonenumber1}',
            to='+{phonenumber2}'
        )
        print(message.status)
        break


