##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import datetime as dt
import smtplib
from email.message import EmailMessage
MY_EMAIL = "dmsqo122@kakao.com"
MY_PASSWORD = "!qodmsakdejr9195"
PORT = 465

# 1. Update the birthdays.csv
birthday_df = pd.read_csv('birthdays.csv')
new_row = {"name":"Eunbae","email":"dmsqo122@naver.com","year": 1995,"month": 7,"day": 31}

birthday_df.iloc[1,:] = new_row

birthday_df.loc[2] = ["BaeBae", "dmsqo122@naver.com", 1990, 7, 31]



birthday_df.month = birthday_df.month.astype('int')
birthday_df.day = birthday_df.day.astype('int')
birthday_df.year = birthday_df.year.astype('int')

now = dt.datetime.now()
dt_day = now.day
dt_month = now.month

for idx, row in birthday_df.iterrows():
    if row.month == dt_month and row.day == dt_day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", mode='r', encoding='utf-8') as file:
            letter = file.read().replace('[NAME]',row['name'])
        with smtplib.SMTP_SSL("smtp.kakao.com",port=PORT) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            message = EmailMessage()
            message.set_content(letter)
            message["Subject"] = "Congratulations!"
            message["From"] = MY_EMAIL
            message["To"] = row.email
            connection.send_message(message)
    


    


