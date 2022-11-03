import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver')

browser.get('https://www.whoscored.com/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_xpath('//[@id="qc-cmp2-ui"]/div[2]/div/button[2]') 
cookies.click()
time.sleep(2)

ucl = browser.find_element_by_xpath('//*[@id="popular-tournaments-list"]/li[19]/a') 
ucl.click()
time.sleep(2)


change_date = browser.find_element_by_xpath('//[@id="date-controller"]/a[1]') 
change_date.click()
time.sleep(2)

titre = browser.find_elements_by_tag_name('h2')
list_anim = [elem.text for elem in titre]
print(list_anim)

stylemangas = browser.find_elements_by_class_name('stl')
list_style = [elem.text for elem in stylemangas]
print(list_style)

genremangas = browser.find_elements_by_class_name('gr')
list_genre = [elem.text for elem in genremangas]
print(list_genre)

synopsismangas = browser.find_elements_by_class_name('text-justify')
list_synopsis = [elem.text for elem in synopsismangas]
print(list_synopsis)

df = pd.DataFrame(list(zip(list_anim, list_style, list_genre, list_synopsis)),
               columns =['titre', 'style', 'genre', 'synopsis'])

filepath = Path('')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()