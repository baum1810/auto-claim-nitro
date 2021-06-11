import undetected_chromedriver as uc
uc.install()

import os
import time 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
print('coded by baum#9149')
token = input("Token: ")
link = input("Gift Link: ")
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://discord.com/login')






time.sleep(2)
script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 0);
            setTimeout(() => {
            location.reload();
            }, 0);
            }
            """
driver.execute_script(script + f'\nlogin("{token}")')
time.sleep(10)
driver.get(link)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="popout_2"]/div/div[1]/div[2]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/button[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/input').send_keys("5297500601008568")
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/input').send_keys("5/23")
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/input').send_keys("468")
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/input').send_keys("John Davis")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/input').send_keys("NewTown Steet 68")
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[4]/div/div[2]/div/input').send_keys("New work")
baum = driver.find_element_by_xpath('//*[@id="react-select-3-input"]')
baum.send_keys("New York")
baum.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[5]/div[2]/div[2]/div/input').send_keys("10010")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/div/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/label/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/button').click()

