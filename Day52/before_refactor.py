from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
URL = "https://www.instagram.com/"
USER_NAME= "blahblah@kakao.com"
USER_PASSWORD = "blahblah"
SIMILAR_ACCOUNT = "thekfa"

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(URL)

time.sleep(5)

username = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(1) > div > label > input')
username.send_keys(USER_NAME)

userpassword = driver.find_element(By.NAME,'password')
userpassword.send_keys(USER_PASSWORD)
userpassword.send_keys(Keys.ENTER)

time.sleep(10)

after_btn = driver.find_element(By.CLASS_NAME, '_ac8f')
after_btn.click()

time.sleep(10)

after_btn2 = driver.find_element(By.CSS_SELECTOR,'._a9-v ._a9_1')
after_btn2.click()

time.sleep(5)

btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
btn.click()

time.sleep(5)

search_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
search_input.send_keys(SIMILAR_ACCOUNT)
time.sleep(5)

account = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
account.click()
time.sleep(5)

follow_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
follow_btn.click()
time.sleep(5)
i = 1
while True:
    try:
        each_follower = driver.find_element(By.XPATH,f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
    except:
        break
    else:
        print("follow 가능")
        each_follower.click()
        time.sleep(5)
        i += 1

time.sleep(5)
driver.quit()





