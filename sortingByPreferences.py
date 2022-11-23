# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:34:22 2022

@author: kelly
"""
import pandas as pd
# runtime, max time, min time, preferences, display results, button to popup trailers
# Preferences - genre, year of release, ratings, dropdown menu/checkboxes for list of filters,

# assumed that GUI inputs will output a dictionary with set attributes
df = pd.read_csv('FinalDatabase.csv', sep=',', header=0, low_memory = False)




df["category"] = df["category"].str.replace("[' ]","")
df['category'] = df.category.apply(lambda x: x[1:-1].split(','))

df["nconst"] = df["nconst"].str.replace("[' ]","")
df['nconst'] = df.nconst.apply(lambda x: x[1:-1].split(','))

df["primaryName"] = df["primaryName"].str.replace("[' ]","")
df['primaryName'] = df.primaryName.apply(lambda x: x[1:-1].split(','))

df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'])
df['numVotes'] = pd.to_numeric(df['numVotes'])


userPreference = {"mintime": 120, "maxtime": 125,  "genre": "horror", "yearRelease": 2010, }


# finding movies with runtime between 115 and 120
df = df.loc[(df['runtimeMinutes']<=userPreference["maxtime"]) & (df['runtimeMinutes']>=userPreference["mintime"])]

# sorting with numVotes as top priority, avg rating as 2nd priority
df = df.sort_values(by=['numVotes', 'averageRating'])

# finding all movies with horror genre as well - doing priority for this would need more thought
df['genres'] = df['genres'].str.lower()
df = df.loc[df['genres'].str.contains('horror')]


dfBest = df.head(10)
dfWorst = df.tail(10)
    
print(dfBest)
print(dfWorst)
