#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:32:14 2022

@author: ppaulkimm
"""

import webbrowser
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options



topic_search = input("Enter what movie to watch? ")
topic_search2 = topic_search.replace(' ', '+')
# driver = webdriver.Chrome(ChromeDriverManager().install())
s = Service("/Users/ppaulkimm/Desktop/Fall 2022/ME 396P - Prog/Project/chromedriver")
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service = s, options = options)




driver.get("https://www.imdb.com/find?q=" + topic_search2)

# Assumption: The movie we're looking for is the first result that comes up
try:
    movie_link = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div[1]/a')
except NoSuchElementException:
    movie_link = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a')
movie_link.click()



# Once we get to movie info page, use BS4 to scrape info
current_url = driver.current_url
html = requests.get(current_url)
html = html.text
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
names = soup.select(".ipc-inline-list__item .ipc-metadata-list-item__list-content-item--link")


director = names[0].get_text()
print(f"Director: {director}")

movie_summary = soup.select(".gXUyNh")[0].get_text()
print(f"Summary: {movie_summary}") 


trailer_link = ''

try:
    trailer_link = driver.find_element(By.XPATH, '//*[@id="imdbnext-vp-jw-inline"]/div[2]/div[4]/video' )
except NoSuchElementException:
    # trailer_link = driver.find_element(By.XPATH, '//*[@id="imdbnext-vp-jw-inline"]/div[2]/div[4]/video' )
    pass
    print("There's no existing trailer for this movie/show on IMDB!")    
    
    
if trailer_link != '':  
    src = trailer_link.get_attribute('src')
    print(src)

# webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(src,new=0, autoraise=True)
# webbrowser.open_new(src)
driver2 = webdriver.Chrome(service = s)
driver2.get(src)
