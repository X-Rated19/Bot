import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='/Users/atabekov/PycharmProjects/pythonProject/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get('https://kolesa.kz')

    add_new = driver.find_element(By.CLASS_NAME, "fi-add-big").click()
    login_input = driver.find_element(By.ID, 'login')
    login_input.send_keys('87077423143')
    login_input.send_keys(Keys.ENTER)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('Atabekov19')
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()