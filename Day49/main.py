from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

driver.get(URL)

login = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
login.click()

user_id = driver.find_element(By.ID, 'username')
user_id.send_keys("dmsqo122@naver.com")

user_password = driver.find_element(By.ID, 'password')
user_password.send_keys("!qodmsakdejr")
btn = driver.find_element(By.CSS_SELECTOR, 'div button')
btn.click()
time.sleep(5)

company_list = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container li a')

for company in company_list:
    print(company.text)
    company.click()
    time.sleep(5)
    job_save_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    job_save_btn.click()

time.sleep(5)
driver.quit()
