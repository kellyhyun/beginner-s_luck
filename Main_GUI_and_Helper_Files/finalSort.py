# -*- coding: utf-8 -*-

import pandas as pd
import seleniumMain

def initialize(dictionaryPreferences):
    df = pd.read_csv('FinalDatabase.csv', sep=',', header=0, low_memory = False)
    df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'])
    df['numVotes'] = pd.to_numeric(df['numVotes'])
    df["category"] = df["category"].str.replace("[' ]","")
    df['category'] = df.category.apply(lambda x: x[1:-1].split(','))
    df["primaryName"] = df["primaryName"].str.replace("['","", regex = False)
    df["primaryName"] = df["primaryName"].str.replace("']","", regex = False)
    df["primaryName"] = df["primaryName"].str.replace(" '","", regex = False)
    df["primaryName"] = df["primaryName"].str.replace("',",",", regex = False)
    df['primaryName'] = df.primaryName.apply(lambda x: x[0:-1].split(','))
    df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'])
    df['startYear'] = pd.to_numeric(df['startYear'])
    df['numVotes'] = pd.to_numeric(df['numVotes'])
    df.insert(len(df.columns),"weight", 0)
    df['genres'] = df.genres.apply(lambda x: x[0:].split(','))
    return df
    #initializing all the attributes from the dataframe
def sortTime (newdf, dictionaryPreferences):
    maxtime = dictionaryPreferences['maxtime'] 
    mintime = dictionaryPreferences['mintime']
    newdf = newdf.drop(newdf[newdf['runtimeMinutes'] > maxtime].index)
    
    for index, row in newdf.iterrows():
        if mintime <= row["runtimeMinutes"] <= maxtime:
            row["weight"] = 5
        else:
            average = (mintime + maxtime)/2
            row["weight"] = (1 - (abs(row["runtimeMinutes"]-average)/422))*5
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf
'''
functions sortTime(), sortYear, and sortRating follow the same sorting principle
where it finds the mean value of the corresponding attribute
Then, the corresponding attribute of the movie of interest is subtracted by the mean value
And this value is divided by a specific number***
specific number*** can be any of the following: max difference allowed for movies in (runtime, year, rating)
Once this is found, weight of the attribute is calculated by (1 - quotient from previous calculation)
Then the output is added to a new dataframe
'''
def sortGenre (weight, newdf, dictionaryPreferences):
    usergenre = dictionaryPreferences['genres'] 
    
    for index, row in newdf.iterrows():
        match = 0
        for i in row["genres"]:
            if i in usergenre:
                match += 1
        row["weight"] = match/len(usergenre)*weight
        #everytime the genre inputted matches the described genre for each movie
        # correlate the weight to the corresponding movie, where weight is equal to # of genres desired by user that movie also has / Total

        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf

def sortYear (weight, newdf, dictionaryPreferences):
    maxyear = dictionaryPreferences['maxyear'] 
    minyear = dictionaryPreferences['minyear']
    
    for index, row in newdf.iterrows():
        if minyear <= row["startYear"] <= maxyear:
            row["weight"] = weight
        else:
            average = (minyear + maxyear)/2
            row["weight"] = (1 - (abs(row["startYear"]-average)/107))*weight
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf

def sortRating (weight, newdf, dictionaryPreferences):
    maxrating = dictionaryPreferences['maxrating'] 
    minrating = dictionaryPreferences['maxrating']
    
    for index, row in newdf.iterrows():
        if minrating <= row["averageRating"] <= maxrating:
            row["weight"] = weight
        else:
            average = (minrating + maxrating)/2
            row["weight"] = (1 - (abs(row["averageRating"]-average)/9.7))*weight
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf

def combineSort(newdf, preferencesImportance, dictionaryPreferences):
    newdf = sortTime(newdf, dictionaryPreferences)
    newdf = newdf.sort_values(by=['weight'],ascending=False)
    newdf = newdf.head(1000)
    
    for rank in range(1,4):
        ranktoweight = {1:3, 2:2, 3:1}
        if preferencesImportance[rank] == "Genres":
            print("genres")
            newdf = sortGenre(ranktoweight[rank], newdf, dictionaryPreferences)
        if preferencesImportance[rank] == "Year":
            print("year")
            newdf = sortYear(ranktoweight[rank], newdf, dictionaryPreferences)
        if preferencesImportance[rank] == "Rating":
            print("rating")
            newdf = sortRating(ranktoweight[rank], newdf, dictionaryPreferences)
    newdf = newdf.sort_values(by=['weight'],ascending=False)
    return newdf

'''
Once the new dataset is created, all the attributes are combined under combineSort(), where
each atttribute is then sorted based on their given weight.
Weights for each attribute were calculated in their own respective functions
'''
def movieList (newdf, preferencesImportance, dictionaryPreferences):
    newdf = combineSort(newdf, preferencesImportance, dictionaryPreferences)
    top = newdf.head(10)
    mList = []
    for index, row in top.iterrows():
        mList.append(newdf.loc[index,"primaryTitle"])
    refreshed = newdf.iloc[10: , :]
    return top, refreshed, mList

'''
movieList() function outputs the sorted data, where it returns the top 10 movies, followed by refreshed lists 
'''
