from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome('Driver Location', options=options)

# Hansot URL Link
URL = 'https://www.hsd.co.kr/menu/menu_list'


# Open URL
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=3)

btn_more = driver.find_element_by_class_name("c_05")

# Click Button
try:
    for i in range(50):
        btn_more.click()
        time.sleep(2)
except:
    print("종료되었습니다")

# Parsing by lxml for Render Speed
soup = BeautifulSoup(driver.page_source, 'lxml')
title = soup.select('h4.h.fz_03')
price = soup.select("div.item-price > strong")
time.sleep(0.3)

title_list = []
price_list = []

for i in range(len(title)):
    title_list.append(title[i].text.strip())
    price_list.append(price[i].text.strip()+"원")
    time.sleep(0.3)

df = pd.DataFrame({'Menu' : title_list, 'Price' : price_list})

df.to_csv('HansotMenu.csv', header=False, index=False, encoding='utf-8-sig')
