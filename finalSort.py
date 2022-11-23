# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:34:22 2022

@author: kelly
"""
import pandas as pd

def initialize():
    df = pd.read_csv('FinalDatabase-MovieOnly.csv', sep=',', header=0, low_memory = False)
    df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'])
    df['numVotes'] = pd.to_numeric(df['numVotes'])
    df["category"] = df["category"].str.replace("[' ]","")
    df['category'] = df.category.apply(lambda x: x[1:-1].split(','))
    df["primaryName"] = df["primaryName"].str.replace("[' ]","")
    df['primaryName'] = df.primaryName.apply(lambda x: x[1:-1].split(','))
    df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'])
    df['startYear'] = pd.to_numeric(df['startYear'])
    df['numVotes'] = pd.to_numeric(df['numVotes'])
    df.insert(len(df.columns),"weight", 0)
    
    global dictionaryPreferences
    dictionaryPreferences = {"valid": False, "maxtime": 201, "mintime":200, "genres":["Horror", "Thriller", "Comedy"], "minyear":1990, "maxyear": 2000, "maxrating":8.5, "minrating":8.4}
    global preferencesImportance
    preferencesImportance = {1:"Rating", 2:"Genres", 3:"Year", "valid":False}
    return df

def sortGenre (weight, newdf):
    global dictionaryPreferences
    usergenre = dictionaryPreferences['genres'] 
    
    newdf['genres'] = newdf.genres.apply(lambda x: x[0:].split(','))
    for index, row in newdf.iterrows():
        match = 0
        for i in row["genres"]:
            if i in usergenre:
                match += 1
        row["weight"] = match/len(usergenre)*weight
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf

def sortYear (weight, newdf):
    global dictionaryPreferences
    maxyear = dictionaryPreferences['maxyear'] 
    minyear = dictionaryPreferences['minyear']
    
    for index, row in newdf.iterrows():
        if minyear <= row["startYear"] <= maxyear:
            row["weight"] = weight
        else:
            average = (minyear + maxyear)/2
            row["weight"] = 1 - (abs(row["startYear"]-average)/107)
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf

def sortRating (weight, newdf):
    global dictionaryPreferences
    maxrating = dictionaryPreferences['maxrating'] 
    minrating = dictionaryPreferences['maxrating']
    
    for index, row in newdf.iterrows():
        if minrating <= row["averageRating"] <= maxrating:
            row["weight"] = weight
        else:
            average = (minrating + maxrating)/2
            row["weight"] = 1 - (abs(row["averageRating"]-average)/9.7)
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf


def combineSort(newdf):
    global preferencesImportance
    for rank in range(1,4):
        ranktoweight = {1:3, 2:2, 3:1}
        if preferencesImportance[rank] == "Genres":
            print("genres")
            newdf = sortGenre(ranktoweight[rank], newdf)
        if preferencesImportance[rank] == "Year":
            print("year")
            newdf = sortYear(ranktoweight[rank], newdf)
        if preferencesImportance[rank] == "Rating":
            print("rating")
            newdf = sortRating(ranktoweight[rank], newdf)
    newdf = newdf.sort_values(by=['weight'],ascending=False)
    return newdf

def movieList (newdf):
    top = newdf.head(10)
    mList = []
    for index, row in top.iterrows():
        mList.append(newdf.loc[index,"primaryTitle"])
    return mList

df = initialize()
df = combineSort(df)
mList = movieList(df)
