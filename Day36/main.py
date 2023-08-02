import requests
import datetime as dt
from datetime import timedelta
import os
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

MY_STOCK_API = "blahblah"
MY_NEWS_API = "blahblah"

# 어제와 그제의 주가 정보 출력을 위한 코드 

TWILIO_API_KEY= "blahblah"
account_sid = "blahblah"
auth_token = "blahblah"





yesterday = str(dt.date.today() - timedelta(days=1))
prevday = str(dt.date.today() - timedelta(days=2))
# print(yesterday)
# print(prevday)


stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": MY_STOCK_API
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
yesterday_dt = float(stock_data[yesterday]["4. close"])
prevday_dt = float(stock_data[prevday]["4. close"])
# print(yesterday_dt)
# print(prevday_dt)

# 주가 변화율 공식 
stock_change = (yesterday_dt - prevday_dt)/prevday_dt * 100
# stock_change = -10.5

# print(stock_change)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_params = {
    "q": COMPANY_NAME,
    "apiKey":MY_NEWS_API
}


news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()['articles'][:3]
three_headlines = [f"HeadLine: {each_data['title']}\nBrief:{each_data['description']}"for each_data in news_data]
# print(three_headlines)


#TWILIO API 사용하기 
client = Client(account_sid, auth_token)

if stock_change <= -5 :
    percent = f"{STOCK}:🔻{stock_change} %"
    for headline in three_headlines:
        message = client.messages.create(
            body=f"{percent}\n{headline}",
            from_="blahblah",
            to="blahblah"
        )
elif stock_change >= 5:
    percent = f"{STOCK}: 🔺{stock_change} %"
    for headline in three_headlines:
        message = client.messages.create(
            body=f"{percent}\n{headline}",
            from_="blahblah",
            to="blahblah",
        )


        
