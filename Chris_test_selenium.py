# Chris's code for presentation demo

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
s = Service("/Users/Christopher/Desktop/ME396P/chromedriver")
options = Options()
# --------- window stays open when code runs
options.add_experimental_option("detach", True)
# --------- window doesn't pop up when code runs
# options.add_argument("--headless")
driver = webdriver.Chrome(service=s, options=options)


# --------------------  GETTING MOVIE INFO -----------------
def scrape_movie_info(movie_name):
    # ----------------  SET UP CHROMEDRIVER ----------------
    driver.get("https://www.imdb.com/find?q=" + movie_name + "&ref_=nv_sr_sm")
    # Assumption: The movie we're looking for is the first result that comes up
    try:
        movie_link = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div[1]/a')
    except NoSuchElementException:
        movie_link = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a')
    movie_link.click()

    # Once we get to movie info page, use BS4 to scrape info
    current_url = driver.current_url

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    html = requests.get(current_url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())

    # ---------------   LOOK FOR DATA ------------------------
    print('-------------------------------------------------------------------------------------')
    names = soup.select(".ipc-inline-list__item .ipc-metadata-list-item__list-content-item--link")
    director = names[0].get_text()
    print(f"Director: {director}")

    movie_summary = soup.select(".gXUyNh")[0].get_text()
    print(f"Summary: {movie_summary}")

    trailer_html = ''
    try:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="imdbnext-vp-jw-inline"]/div[2]/div[4]/video')
        trailer_link = trailer_html.get_attribute('src')
    except NoSuchElementException:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[2]/div[2]/div[2]/div[1]/div[1]/a')
        trailer_link = trailer_html.get_attribute('href')
    print(f"Trailer link: trailer_link")

    if trailer_link == '':
        print("There's no existing trailer for this movie/show on IMDB!")

def scrape_movies_list(movie_names_list):
    for movie in movie_names_list:
        scrape_movie_info(movie)


if __name__ == '__main__':
    list_of_movies = []
    search_movie = input("What movie would you like information about?")
    list_of_movies.append(search_movie)
    done = False
    while not done:
        keep_going = input("Anything else? [y/n]")
        if keep_going == 'n':
            done = True
        if keep_going == 'y':
            search_movie = input("What movie would you like information about?")
            list_of_movies.append(search_movie)
    print(list_of_movies)
    scrape_movies_list(list_of_movies)