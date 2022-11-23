# G06: Beginner's luck
# Final Project: Title
## Members
  Lawrence Chung, Christopher Hong, Kelly Hyun, Paul Kim

## Overview
Have you ever been annoyed because you had to go to a meeting halfway through watching a movie at home? Our program can give you a list of movies that you can finish just in time for your next schedule, so you don't have to care about runtime when you choose a movie to watch. There are a lot of websites online, such as [iMDB]([url](https://www.imdb.com/?ref_=nv_home)) that allow you to search for movies based on rating, number of votes, director, genre and more. However, to some movie-lovers' frustration, these websites lack a way to filter movies by runtime. 

Using packages such as [Selenium]([url](https://www.selenium.dev/)) and [BeautifulSoup4]([url](https://pypi.org/project/beautifulsoup4/)), our program is able to find you a list of recommended movies that you can finish just before you leave for your next schedule. In addition, you may filter the results using different criteria such as number of user votes, average rating, genre, and more to find the best movie for you more easily!

## Packages used

### Selenium
Selenium is a web scraping package that is most commonly used in complex projects. In our project, we use Selenium to navigate through iMDB websites. In more detail, we use Selenium to automate the searching and clicking actions.

NOTE: In order to utilize Selenium, user needs to download Chromedriver in order to run the codes related to Selenium.
When downloading the driver, make sure to download the correct version corresponding to your chrome.

The link to download Chromedriver can be found here: https://chromedriver.chromium.org/downloads

### BeautifulSoup4
BeautifulSoup4, or BS4, is another web scraping package that is known to be more efficient for smaller projects. BS4 tends to run a bit quicker than Selenium when dealing with a static webpage. We chose BS4 over Selenium to scrape information from the destination pages' html codes to leverage this strength.
### Pandas
We all know about Pandas. Our group used pandas to filter through the entire iMDB film database to create our own, more selective database of movies. Each time the code is run, we will sort through the database using pandas to find the best movies as well!

## Functions

### Basics
The most basic building block of our projects looks like this (all data based on iMDB).

Input:
```
Movie Name
```
Output:
```
Director
Main Cast
Average Rating
Number of Votes
Genre
Summary
```

### Runtime?
From now on, you'll always be able to satisfyingly finish a movie before you have to head out. Simply input how much time you have, we'll find a few good ones you could squeeze in that time frame.
### Additional Preferences

