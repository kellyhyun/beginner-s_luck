# G06: Beginner's luck
# Final Project: Movie Generator
## Members
  Lawrence Chung, Christopher Hong, Kelly Hyun, Paul Kim


## Overview
Have you ever been annoyed because you had to go to a meeting halfway through watching a movie at home? Our program can give you a list of movies that you can finish just in time for your next schedule, so you don't have to care about runtime when you choose a movie to watch. There are a lot of websites online, such as [iMDB]([url](https://www.imdb.com/?ref_=nv_home)) that allow you to search for movies based on rating, number of votes, director, genre and more. However, to some movie-lovers' frustration, these websites lack a way to filter movies by runtime. 

Using packages such as [Selenium]([url](https://www.selenium.dev/)) and [BeautifulSoup4]([url](https://pypi.org/project/beautifulsoup4/)), our program is able to find you a list of recommended movies that you can finish just before you leave for your next schedule. In addition, you may filter the results using different criteria such as number of user votes, average rating, genre, and more to find the best movie for you more easily!

## Running Code Locally

In order to make sure this code runs on your own laptop, there are a couple of things that you may have to tweak. Make sure you get this right, or it will continue to pop errors!

1. Download chromedriver: https://chromedriver.chromium.org/downloads. Make sure you get the right version that corresponds to your chrome browser!
3. Navigate to one of our files: seleniumMain.py and change line 18 to s = Service("Your/Chromedriver/Path")
4. You may have to adjust the request header depending on your browser. Here is a link to instructions on how to find your own http header. https://mkyong.com/computer-tips/how-to-view-http-headers-in-google-chrome/#:~:text=To%20view%20the%20request%20or,displayed%20on%20the%20right%20panel.
5. Once you get your http header, navigate to line 44 of the same file and change it to headers = {'User-Agent': 'Your http header'}
6. Once those are completed, you're free to go! Run mainKivy.py, our main code.

Note that our program takes a couple of minutes to run. While the GUI shows "loading," feel free to go grab a cup of water and get ready for a movie!

## Packages used

### Selenium
Selenium is a web scraping package that is most commonly used in complex projects. In our project, we use Selenium to navigate through iMDB websites. In more detail, we use Selenium 4*** to automate the searching and clicking actions.

NOTE: In order to utilize Selenium, user needs to download Chromedriver in order to run the codes related to Selenium.
When downloading the driver, make sure to download the correct version corresponding to your chrome.
In order for the code to run properly, make sure the service for the Chromedriver is in an executable path.

```
s = Service("appropriate pathname")
```

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
While this isn't considered a package, IMDB database was downloaded to facilitate the filtering process of the code when searching for movies. This significantly reduces the runtime of the code as it reduces the amount of webscraping that needs to take place to gather all the necessary information. The csv file of the database can be found in the file labeled 'FinalDatabase.csv'

## Creating our Database (creatingDatabase.py)

### IMDB Databases
All information from our finalDatabase.csv are taken from IMDB datasets found here: https://datasets.imdbws.com/.
The file creatingDatabase.py is separated into three sections because the IMDB datasets are large and difficult to work with all at once. 
If running this file on your machine, be sure to change the file names of the datasets. 
```
First Section:
  title.basics.tsv.gz and title.ratings.tsv.gz from the IMDB datasets are used for this section.
  Create database with columns that are specific to each title. 
  Here we filtered out titles that have super small runtimes, titles that are not movies, and titles with fewer than 10,000 votes because we did not want to include obsure movie titles. 
  
  The columns are as follows: 
    tconst - unique alphanumeric identifier [taken from title.basics and title.ratings]
    titleType - type of format of the title (movie, short, tv-show, etc.) [taken from title.basics]
    primaryTitle - more popular title [taken from title.basics]
    startYear - release year of the title [taken from title.basics]
    runtimeMinutes - runtime of title [taken from title.basics]
    genres - has up to three genres associated with this title [taken from title.basics]
    averageRating - weighted average of individual user ratings [taken from title.ratings]
    numVotes - number of votes the title has recieved [taken from title.ratings]

Second Section:
  title.principals.tsv (connecting all names to titles), name.basics.tsv, and the database that were created in section 1 were used to create a database of what the crew in each movie did and their names. 
  This section creates a database that has the movie in as many rows as the number of people in the crew. 

Third Section:
  The databases from sections 1 and 2 are used for this section.
  We read db2.csv and drop some columns (such as birthYear, deathYear, job, etc.) because they are unneeded and will increase the speed this section. 
  We then put the names and categories (roles) of the crew in a list, where the indexes still match between the two for all actors, actresses, and directions. These lists are put in their own databases and then merged with the database from section 1. 
    For example, the director of Inception is Christopher Nolan, so his name is in the second index of the names list and 'director' is in the second index of the category list. 
 
 The columns added are as follows:
    names - list of the names of all the crew [taken from name.basics and title.principals]
    categories - list of all categories of crew members [taken from name.basics and title.principals]

```

## Functions

### Basics
The most basic building block of our projects looks like this (all data based on iMDB).

Input:
```
Movie Name
```
Output:
```
Summary
Runtime
Rating (Votes)
Year 
Genre
Crew
Trailer Link
```

### Runtime?
From now on, you'll always be able to satisfyingly finish a movie before you have to head out. The maximum runtime preferred will be set as a hard limit, so you'll definitely be able to finish the movie before you leave. 
```
Otherwise:
  Weight = (1 - (| Movie Runtime - Average Runtime |) / (Total Difference of Runtimes)) * 200
    Where 422 is the total difference of maximum and minimum possible runtimes.
  200 is the weight we decided for the runtime because it is the most important preference for our app. 
```

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
    
    
Weights are added together and sorted to list the movies best suited to the user.
```    
Once the precedence is set, the list of movies suggested should follow the structure above and output them in a correct order.


### Limitations and Future work
While the code allows for a few functionalities that generates numerous outputs, there are still areas for improvement. Some of the areas that can be improved are as follows:

1. Implement a feature where trailer link generated can be clickable so that it can be directed to a webpage with the trailer loaded for viewing. Another method to approach this concept is to preload the trailer videos into the GUI, where the user has the option to directly click on the corresponding video to view. 

2. Add a feature where the runtime, rating, and year attributes that be toggled with sliding bars. This way, the user would not have to input the values manually.

3. Include an option, where it asks the user to click on a hyperlink that takes him/her directly to the movie's IMDB webpage for further information.

4. Utilize lxml parser instead of html.parser to further increase the webscraping speed.

