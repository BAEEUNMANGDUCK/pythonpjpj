import requests
from email.message import EmailMessage
import smtplib
from datetime import datetime
import time 

MY_LAT = 37.566536 # Your latitude
MY_LONG = 126.977966 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


    

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
time_now = datetime.utcnow()
print(time_now.hour)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def send_message():
    # 우주 정거장 위치가 허용 오차 범위 안에 있고, 현재 시각이 해가 뜨기 전 밤인지 확인하는 조건문
    # 조건에 만족하면 아래의 명령문 실행 
    if (MY_LAT - 5 <=iss_latitude <= MY_LAT + 5)\
        and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)\
        and sunset <= time_now.hour <= sunrise:
            with smtplib.SMTP_SSL("smtp.kakao.com", port=465) as connection:
                connection.login(user="example@example.com", password="blahblah")
                message = EmailMessage()
                message.set_content("ISS is above")
                message["Subject"] = "ISS!!!"
                message['From'] = "example@example.com"
                message['To'] = "example2@example.com"
                connection.send_message(message)

while True:
    # 5초마다 조건에 만족하는지 확인
    time.sleep(5)
    print("Hello!")
    send_message()