# Selenium Web Driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get("https://www.coupang.com/vp/products/7405993243?itemId=19178499695&vendorItemId=86296432531&pickType=COU_PICK&q=%EA%B0%A4%EB%9F%AD%EC%8B%9C%EC%9B%8C%EC%B9%98&itemsCount=36&searchId=fb876066cee942c480d042a6acb53b0f&rank=3&isAddedCart=")
# price = driver.find_element(By.CSS_SELECTOR, '.total-price strong')
# print(price.text)

# driver.get('https://www.python.org/')

# search_bar = driver.find_element(By.NAME,"q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')


time.sleep(2)

driver.quit()