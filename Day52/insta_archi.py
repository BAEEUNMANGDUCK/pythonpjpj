from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time



class InstaFollower:
    def __init__(self,url):
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920x1080')
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.driver.get(url)
        time.sleep(5)


    def login(self,name, pwd):
        username = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
        username.send_keys(name)

        userpassword = self.driver.find_element(By.NAME, 'password')
        userpassword.send_keys(pwd)
        userpassword.send_keys(Keys.ENTER)

        time.sleep(10)

    def find_followers(self, simul_account):
        after_btn = self.driver.find_element(By.CLASS_NAME, '_ac8f')
        after_btn.click()

        time.sleep(10)

        after_btn2 = self.driver.find_element(By.CSS_SELECTOR, '._a9-v ._a9_1')
        after_btn2.click()

        time.sleep(5)

        btn = self.driver.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
        btn.click()

        time.sleep(5)

        search_input = self.driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search_input.send_keys(simul_account)
        time.sleep(5)

        account = self.driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
        account.click()
        time.sleep(5)

    def follow(self):
        follow_btn = self.driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
        follow_btn.click()
        time.sleep(5)
        i = 1
        while True:
            try:
                each_follower = self.driver.find_element(By.XPATH,
                                                    f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
            except:
                break
            else:
                print("follow 가능")
                each_follower.click()
                time.sleep(5)
                i += 1

        time.sleep(5)
        self.driver.quit()

















