from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.python.org/")

times = [time.text for time in driver.find_elements(By.CSS_SELECTOR, '.last .menu li time')]
schedules = [schedule.text for schedule in driver.find_elements(By.CSS_SELECTOR, '.last .shrubbery ul li a')[:5]]

events = {idx: {'time': time, 'name': schedule} for idx, time, schedule in zip(range(5), times, schedules)}

print(events)

driver.quit()
