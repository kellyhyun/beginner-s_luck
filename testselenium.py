#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:32:14 2022

@author: ppaulkimm
"""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
# from webdriver_manager.chrome import ChromeDriverManager




# url= 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr'

topic_search = input("Enter what movie to watch? ")
topic_search2 = topic_search.replace(' ', '+')
# driver = webdriver.Chrome(ChromeDriverManager().install())
s = Service("/Users/ppaulkimm/Desktop/Fall 2022/ME 396P - Prog/Project/chromedriver")
driver = webdriver.Chrome(service = s)

# for i in range(1):
#     url = driver.get("https://www.imdb.com/find?q=" + topic_search + "&ref_=nv_sr_sm" + str(i))

driver.get("https://www.imdb.com/find?q=" + topic_search2 + "&ref_=nv_sr_sm")

link = driver.find_element(topic_search)
link.click()

# try:
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "Keywords"))
#     element.click()
#     # webdriver.findElement(By.xpath("//a[@href='/docs/configuration']")).click();
#     # element = driver.find_element_by_partial_link_text(topic_search)
#     # element.click()

# except:
#     time.sleep(5)
#     driver.quit()

    # '''
    # Above shows how to navigate through webpages externally, pops up a chrome tab
    # and once the movie title is inputted, searchs through the search tab
    
    # Once this has been completed, it clicks the button "Titles" and takes you to the next page
    # '''

    
