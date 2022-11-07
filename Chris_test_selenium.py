# Edited by Chris, based on Paul's code

import requests
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time

# imdb url
url= 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr'

# Ask for movie input, search for it on imdb
topic_search = input("Enter what movie to watch? ")
topic_search2 = topic_search.replace(' ', '+')
driver = webdriver.Chrome(executable_path="/Users/Christopher/Desktop/ME396P/beginner-s_luck-main/chromedriver")
driver.get("https://www.imdb.com/find?q=" + topic_search2 + "&ref_=nv_sr_sm")

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
# print(names)

movie_summary = soup.select(".gXUyNh")[0].get_text()
print(f"Summary: {movie_summary}")

