from bs4 import BeautifulSoup
import requests
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()




# 가격 추출 과정 
URL = "https://www.coupang.com/vp/products/7405993243?itemId=19178499695&vendorItemId=86296432531&sourceType=srp_product_ads&clickEventId=83dfa5e9-60cc-4cdd-8b8f-86da02dd6ff0&korePlacement=15&koreSubPlacement=1&q=%EA%B0%A4%EB%9F%AD%EC%8B%9C+%EC%9B%8C%EC%B9%98&itemsCount=36&searchId=dc9ef4f93f2542c695c4100c66b481ed&rank=0&isAddedCart="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6" 
PORT = 465
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")
want_price = 400000

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
raw_price = soup.select_one(selector=".total-price strong").getText()
# 가격
price = int("".join(raw_price.strip("원").split(",")))
print(price)
# 상품 이름
product_name = soup.find(name="h2", class_="prod-buy-header__title").getText()
print(product_name)


if price <= want_price:
    letter = f"{product_name}이 현재 {raw_price}입니다!\n{URL}"
    with smtplib.SMTP_SSL("smtp.kakao.com", port=PORT) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        message = EmailMessage()
        message.set_content(letter)
        message["Subject"] = "가격 알림!"
        message["From"] = MY_EMAIL
        message["To"] = TO_EMAIL
        connection.send_message(message)


