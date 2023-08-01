import datetime as dt
import requests
MY_LAT = 37.566536
MY_LNG = 126.977966
# URL = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url=URL)
# # 올바른 작동을 안할 때 Error를 냄. 
# response.raise_for_status()
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (longitude, latitude)
# print(iss_position)

param = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response2 = requests.get("https://api.sunrise-sunset.org/json",params=param)
response2.raise_for_status()
data = response2.json()['results']
sunrise = data['sunrise'].split('T')[1].split(":")[0]
sunset = data['sunset'].split('T')[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)
    

# # <Response [1XX]> : Hold on
# # <Response [2XX]> : Here you go
# # <Response [3XX]> : Go Away
# # <Response [4XX]> : You screwed up 
# <Response [5XX]> : I screwed up 
