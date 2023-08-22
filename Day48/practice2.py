from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname=driver.find_element(By.NAME, 'fName')
fname.send_keys('Eunbae')
lname=driver.find_element(By.NAME, 'lName')
lname.send_keys('Kim')
email=driver.find_element(By.NAME, 'email')
email.send_keys('blahblah@naver.com')
email.send_keys(Keys.ENTER)


time.sleep(5)

driver.quit()
