# Simple Mail Transfer Protocol

import smtplib 
import random
import datetime as dt
from email.message import EmailMessage

my_email = "exmaple@blahblah.com"
password = "exafdalkjafd"
now = dt.datetime.now()
week_day = now.weekday()

with open('quotes.txt') as file:
    my_quotes = [quote.replace('\n', '') for quote in file.readlines()]



with smtplib.SMTP_SSL("smtp.kakao.com", port=465) as connection:
    connection.login(user=my_email, password=password)
    random_quote = random.choice(my_quotes)
    message = EmailMessage()
    message.set_content(f"{random_quote}")
    message["Subject"] = "Eunbae"
    message["From"] = my_email
    message["To"] = "dmsqo122@naver.com"
    
    if week_day == 0:
        connection.send_message(message)



