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

database = pd.read_csv('ourDatabase.csv')

# --------------------  GETTING MOVIE INFO -----------------
def scrape_movie_info_imdb(movie_name):
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
    movie_name_header = soup.find('h1')
    title = movie_name_header.get_text()
    release_year = soup.select(".WIUyh")
    release_year = release_year[0].get_text()

    names = soup.select(".ipc-inline-list__item .ipc-metadata-list-item__list-content-item--link")
    director = names[0].get_text()
    movie_summary = soup.select(".gXUyNh")[0].get_text()

    trailer_html = ''
    try:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="imdbnext-vp-jw-inline"]/div[2]/div[4]/video')
        trailer_link = trailer_html.get_attribute('src')
    except NoSuchElementException:
        trailer_html = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[2]/div[2]/div[2]/div[1]/div[1]/a')
        trailer_link = trailer_html.get_attribute('href')
    string4 = f"Trailer link: {trailer_link}\n"
    if trailer_link == '':
        string4 = "There's no existing trailer for this movie/show on IMDB!"

    string1 = f"{title} ({release_year})\n"
    string2 = f"Director: {director}\n"
    string3 = f"Summary: {movie_summary}\n"


    return title, string1, string2, string3, string4


def scrape_movie_info_database(movie_name):
    r = database.loc[database["primaryTitle"] == movie_name]["averageRating"].to_string(index=False)
    n = database.loc[database["primaryTitle"] == movie_name]["numVotes"].to_string(index=False)
    runtime = database.loc[database["primaryTitle"] == movie_name]["runtimeMinutes"].to_string(index=False)
    string5 = f'Rating: {r} ({n} votes)\n'
    string6 = f'Runtime: {runtime} min\n'
    return string5, string6


def all_together(movie):
    t,s1,s2,s3,s4 = scrape_movie_info_imdb(movie)
    s5,s6 = scrape_movie_info_database(t)
    final_output = s1+s2+s5+s6+s3+s4
    print(final_output)
    return final_output


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
    for movie in list_of_movies:
        final_output = all_together(movie)
