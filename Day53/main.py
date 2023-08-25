from zillow import Zillow
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.842914%2C%22east%22%3A-122.32992%2C%22south%22%3A37.707608%2C%22west%22%3A-122.536739%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScwY139zwkPqV-VYJAj_q9YRToOxWhBsZsgqx-Y5N9wEKkPAQ/viewform?usp=sf_link"
TO_SHEET_URL = "https://docs.google.com/forms/d/1bdHOdjUoJBSPiX8Cz8MXRJGeSq-EL5MkQn12rknoldY/edit?pli=1#responses"
zillow = Zillow(ZILLOW_URL)
links = zillow.get_links()
prices = zillow.get_prices()
addresses = zillow.get_addresses()

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get(GOOGLE_FORM_URL)
time.sleep(5)

for answer1, answer2, answer3 in zip(links, prices, addresses):
    try:
        questions = driver.find_elements(By.CSS_SELECTOR, '.whsOnd')
        questions[0].send_keys(answer1)
        questions[1].send_keys(answer2)
        questions[2].send_keys(answer3)
        time.sleep(2)
        submit_btn = driver.find_element(By.CSS_SELECTOR, '.NPEfkd')
        submit_btn.click()
        time.sleep(2)
    except:
        print("something gones wrong")
        break
    else:
        another_response = driver.find_element(By.CSS_SELECTOR, '.c2gzEf a')
        another_response.click()
        time.sleep(2)
time.sleep(2)

driver.quit()
