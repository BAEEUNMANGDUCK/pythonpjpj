from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_number = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
# articles_number.click()

# # Link click
# view_history = driver.find_element(By.LINK_TEXT,'View history')
# view_history.click()

# Typing

driver.get('https://en.wikipedia.org/wiki/Special:Search')
search = driver.find_element(By.XPATH, '//*[@id="ooui-php-1"]')

search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()