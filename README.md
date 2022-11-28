# G06: Beginner's luck
# Final Project: Movie Generator
## Members
  Lawrence Chung, Christopher Hong, Kelly Hyun, Paul Kim

## Overview
Have you ever been annoyed because you had to go to a meeting halfway through watching a movie at home? Our program can give you a list of movies that you can finish just in time for your next schedule, so you don't have to care about runtime when you choose a movie to watch. There are a lot of websites online, such as [iMDB]([url](https://www.imdb.com/?ref_=nv_home)) that allow you to search for movies based on rating, number of votes, director, genre and more. However, to some movie-lovers' frustration, these websites lack a way to filter movies by runtime. 

Using packages such as [Selenium]([url](https://www.selenium.dev/)) and [BeautifulSoup4]([url](https://pypi.org/project/beautifulsoup4/)), our program is able to find you a list of recommended movies that you can finish just before you leave for your next schedule. In addition, you may filter the results using different criteria such as number of user votes, average rating, genre, and more to find the best movie for you more easily!

## Packages used

### Selenium
Selenium is a web scraping package that is most commonly used in complex projects. In our project, we use Selenium to navigate through iMDB websites. In more detail, we use Selenium 4*** to automate the searching and clicking actions.

NOTE: In order to utilize Selenium, user needs to download Chromedriver in order to run the codes related to Selenium.
When downloading the driver, make sure to download the correct version corresponding to your chrome.

The link to download Chromedriver can be found here: https://chromedriver.chromium.org/downloads

### BeautifulSoup4
BeautifulSoup4, or BS4, is another web scraping package that is known to be more efficient for smaller projects. BS4 tends to run a bit quicker than Selenium when dealing with a static webpage. We chose BS4 over Selenium to scrape information from the destination pages' html codes to leverage this strength.

### Requests
Request is a simple HTTP library package used to send HTTP requests via python.
### Pandas
We all know about Pandas. Our group used pandas to filter through the entire iMDB film database to create our own, more selective database of movies. Each time the code is run, we will sort through the database using pandas to find the best movies as well!

### Kivy
Kivy is an open source GUI development package that allows users to build an app once and be used across all platforms. To utilize this package, the user must create both python and kivy code in order to create applications that are usable. When running the code on an IDE, make sure to restart kernel every time after use to ensure minimal error and issue. 

### Miscellaneous
While this isn't considered a package, IMDB database was downloaded to facilitate the filtering process of the code when searching for movies. This significantly reduces the runtime of the code as it reduces the amount of webscraping that needs to take place to gather all the necessary information. The csv file of the database can be found in the file labeled 'FinalDatabase-MovieOnly.csv'

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
Average Rating
Number of Votes
Runtime
Summary
Trailer link
```

### Runtime?
From now on, you'll always be able to satisfyingly finish a movie before you have to head out. Simply input how much time you have, we'll find a few good ones you could squeeze in that time frame.

### Preference Structuring
Generating movies for the user comes down to user's choice on what attribute he/she would prefer more. To establish such preferences, the schematic below shows how the code is structured:
```
Setting precedence:

1st choice → Multiply the factor by 3
2nd choice → Multiply the factor by 2
3rd choice → Multiply the factor by 1

Genre:

Total = len(choice_list)
If chosen movie has all choices:
  Weight of each genre = 1
Else:
  Weight =  # of genres desired by user that movie also has / Total

Year:

If the chosen year is within range:
  Weight = 1 
Else:
  Mean_range = ( (max_range + min_range) / 2 )
  Then
  Weight = 1 - ( abs(Movie_year - Mean_range) / 107 )
    Where, max difference allowed for movies in years = 107. 
    
Rating: 

If the chosen rating is within range:
  Weight = 1 
Else:
  Mean_rating = ( (max_rating + min_rating) / 2 )
  Then
  Weight = 1 - ( abs(Movie_rating - Mean_rating) / 10 )
    Where, max difference allowed for movies in rating = 10. 
```    
Once the precedence is set, the list of movies suggested should follow the structure above and output them in a correct order.


### Limitations and Future work
While the code allows for a few functionalities that generates numerous outputs, there are still areas for improvement. Some of the areas that can be improved are as follows:

1. Implement a feature where trailer link generated can be clickable so that it can be directed to a webpage with the trailer loaded for viewing. Another method to approach this concept is to preload the trailer videos into the GUI, where the user has the option to directly click on the corresponding video to view. 

2. Add a feature where the runtime, rating, and year attributes that be toggled with sliding bars. This way, the user would not have to input the values manually.

3. Include an option, where it asks the user to click on a hyperlink that takes him/her directly to the movie's IMDB webpage for further information.

4. Utilize lxml parser instead of html.parser to further increase the webscraping speed.

