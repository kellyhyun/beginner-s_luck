import requests
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# ----------------------    WEB SCRAPING    -------------------------
# imdb url
url= 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr'

## ----- NEEDS TO BE CHANGED BY USER ----- ##
s = Service("/Users/kelly/ME396P/chromedriver")
## --------------------------------------- ##

options = Options()
# --------- window stays open when code runs
# options.add_experimental_option("detach", True)
# --------- window doesn't pop up when code runs
options.add_argument("--headless")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver = webdriver.Chrome(service=s, options=options)

# --------------------  GETTING MOVIE INFO -----------------
def scrape_movie_info_imdb(tconst):
    # ----------------  SET UP CHROMEDRIVER ----------------

    driver.get("https://www.imdb.com/title/" + tconst + "/?ref_=fn_al_tt_1")

    # use BS4 to scrape info
    current_url = driver.current_url
    ## --------------------- MIGHT NEED TO BE CHANGED BY USER: CHECK README.MD ----------------
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    ## ----------------------------------------------------------------------------------------
    html = requests.get(current_url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())

    # ---------------   LOOK FOR DATA ------------------------
    print('-------------------------------------------------------------------------------------')
    names = soup.select(".ipc-inline-list__item .ipc-metadata-list-item__list-content-item--link")
    
    try:
        movie_summary = soup.select(".gXUyNh")[0].get_text()
    except:
        movie_summary = "Not avaliable."

    trailer_html = ''
    # Use selenium to find the trailer link
    try:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="imdbnext-vp-jw-inline"]/div[2]/div[4]/video')
        trailer_link = trailer_html.get_attribute('src')
        string4 = f"Trailer link: {trailer_link}\n"
    except NoSuchElementException:
        try:
            trailer_html = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[2]/div[2]/div[2]/div[1]/div[1]/a')
            trailer_link = trailer_html.get_attribute('href')
            string4 = f"Trailer link: {trailer_link}\n"
        except NoSuchElementException:
            string4 = "There's no existing trailer for this movie/show on IMDB!\n"

    string3 = f"Summary: {movie_summary}\n"
    return string3, string4 
