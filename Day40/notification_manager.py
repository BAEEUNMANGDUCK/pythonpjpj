from twilio.rest import Client
from email.message import EmailMessage
import requests
import smtplib
TWILIO_SID =  "blahblah"
TWILIO_AUTH_TOKEN =  "blahblah"
TWILIO_VIRTUAL_NUMBER = "blahblah"
TWILIO_VERIFIED_NUMBER =  "blahblah"
SHEETY_USERS_ENDPOINT = "blahblah"
PORT =  000
MY_EMAIL =  "blahblah"
MY_PASSWORD =  "blahblah"
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_email(self, message):
        user_response = requests.get(url=SHEETY_USERS_ENDPOINT)
        datas = user_response.json()['users']
        print(datas)
        for data in datas:
            with smtplib.SMTP_SSL("smtp.kakao.com", port=PORT) as connection:
                connection.login(MY_EMAIL, MY_PASSWORD)
                my_message = EmailMessage()
                my_message.set_content(message)
                my_message["Subject"] = "Congratulations!"
                my_message["From"] = MY_EMAIL
                my_message["To"] = data["email"]