from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

time_break = time.time() + 60 * 1


def choice_max():
    money = int(driver.find_element(By.ID, 'money').text)
    choice = ""
    if money >= 123456789:
        choice = "buyTime machine"
    elif money >= 1000000:
        choice = 'buyPortal'
    elif money >= 50000:
        choice = 'buyAlchemy lab'
    elif money >= 7000:
        choice = 'buyShipment'
    elif money >= 2000:
        choice = 'buyMine'
    elif money >= 500:
        choice = 'buyFactory'
    elif money >= 100:
        choice = 'buyGrandma'
    elif money >= 15:
        choice = 'buyCursor'

    if len(choice) != 0:
        my_choice = driver.find_element(By.ID, value=choice)
        my_choice.click()


end_of_game = False
schedule.every(1).seconds.do(choice_max)

while not end_of_game:
    schedule.run_pending()
    cookie = driver.find_element(By.ID, 'cookie')
    cookie.click()
    if time.time() > time_break:
        end_of_game = True

cookies_per_seconds = driver.find_element(By.ID,"cps").text
print(cookies_per_seconds)
driver.quit()
