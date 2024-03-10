from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page = requests.get(START_URL)
print(page)

browser.get(START_URL)
time.sleep(10)
stars_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
table = soup.find('table')

temp_list = []
tablerows = table.find_all('tr')

    

for i in range(0,224):
        
    for tr in tablerows:

        td_tags = tr.find_all("li")
        row = [i.text.rstrip() for i in td_tags]
        temp_list.append(row)

star_name = []
radius = []
distance = []
mass = []

for i in range(1,len(temp_list)) :
    star_name.append(i[1])
    radius.append(i[6])
    distance.append(i[5])
    mass.append(i[6])

df = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=["Name","Distance","Mass","Radius"])
print(df)

df.to_csv('Stars.csv',index=True,index_label='Serial_number')