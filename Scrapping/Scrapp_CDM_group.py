import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome('/Users/madeu/CDM/Projet-big-data/chromedriver')

browser.get('https://www.flashscore.com/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_id('onetrust-accept-btn-handler')
cookies.click()
time.sleep(2)

cdm = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/aside/div/div[2]/div[2]/div[3]/div[2]/a/span[2]')
cdm.click()
time.sleep(2)

standings = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/main/div[4]/div[1]/div[3]/div/a[4]')
standings.click()
time.sleep(2)

group = browser.find_elements_by_class_name('tableCellParticipant__name')
list_group= [elem.text for elem in group]
print(list_group)

df = pd.DataFrame(list(zip(list_group)),
                columns =['standings'])

