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
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
# ---------------------     DATABASE STUFF  ------------------------
# # import database of movies
# basics = pd.read_csv('ourDatabase.csv', sep=',', header=0, low_memory = False)
# basics['runtimeMinutes'] = pd.to_numeric(basics['runtimeMinutes'])
# basics['numVotes'] = pd.to_numeric(basics['numVotes'])
#
# # finding movies with correct runtime
# runtime = int(input("How much time do you have?"))
# df = basics.loc[(basics['runtimeMinutes'] <= runtime) & (basics['runtimeMinutes'] >= runtime-10)]
#
# # sorting with numVotes as top priority, avg rating as 2nd priority
# df = df.sort_values(by=['numVotes', 'averageRating'])

# ----------------------    WEB SCRAPING    -------------------------
# imdb url
url= 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr'
s = Service("/Users/Christopher/Desktop/ME396P/beginner-s_luck/chromedriver")
options = Options()
# --------- window stays open when code runs
options.add_experimental_option("detach", True)
# --------- window doesn't pop up when code runs
# options.add_argument("--headless")



# --------------------  GETTING MOVIE INFO -----------------
def scrape_movie_info(movie_name):
    driver = webdriver.Chrome(service=s, options=options)
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

    # ----------------  GETTING TRAILER LINK --------------
    trailer_html = ''

    try:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="imdbnext-vp-jw-inline"]/div[2]/div[4]/video')
        trailer_link = trailer_html.get_attribute('src')

    except NoSuchElementException:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[2]/div[2]/div[2]/div[1]/div[1]/a')
        trailer_link = trailer_html.get_attribute('href')
    print(trailer_link)

    if trailer_link == '':
        print("There's no existing trailer for this movie/show on IMDB!")


    # # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(src,new=0, autoraise=True)
    # # webbrowser.open_new(src)
    # driver2 = webdriver.Chrome(service=s)
    # driver2.get(src)
    #
    # # Ask for movie input, search for it on imdb
    # topic_search = input("Enter what movie to watch? ")
    # topic_search2 = topic_search.replace(' ', '+')
    # scrape_movie_info(topic_search2)

if __name__ == '__main__':
    search_movie = input("What movie would you like to watch?")
    scrape_movie_info(search_movie)