# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:34:22 2022

@author: kelly
"""
import pandas as pd
import seleniumMain

def initialize(dictionaryPreferences):
    df = pd.read_csv('FinalDatabase-MovieOnly.csv', sep=',', header=0, low_memory = False)
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
    # mintime = dictionaryPreferences["mintime"]
    # maxtime = dictionaryPreferences["maxtime"]
    # df = df[(df["runtimeMinutes"] <= maxtime) & (df["runtimeMinutes"]>=mintime)]
    return df

def sortTime (newdf, dictionaryPreferences):
    maxtime = dictionaryPreferences['maxtime'] 
    mintime = dictionaryPreferences['mintime']
    newdf = newdf.drop(newdf[newdf['runtimeMinutes'] > maxtime].index)
    
    for index, row in newdf.iterrows():
        if mintime <= row["runtimeMinutes"] <= maxtime:
            row["weight"] = 200
        else:
            average = (mintime + maxtime)/2
            row["weight"] = (1 - (abs(row["runtimeMinutes"]-average)/422))*200
        newdf.loc[index,"weight"] = newdf.loc[index,"weight"] + row["weight"]
    return newdf

def sortGenre (weight, newdf, dictionaryPreferences):
    usergenre = dictionaryPreferences['genres'] 
    
    for index, row in newdf.iterrows():
        match = 0
        for i in row["genres"]:
            if i in usergenre:
                match += 1
        row["weight"] = match/len(usergenre)*weight
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

def movieList (newdf, preferencesImportance, dictionaryPreferences):
    newdf = combineSort(newdf, preferencesImportance, dictionaryPreferences)
    top = newdf.head(10)
    mList = []
    for index, row in top.iterrows():
        mList.append(newdf.loc[index,"primaryTitle"])
    refreshed = newdf.iloc[10: , :]
    return top, refreshed, mList

# def returnTopRefreshedMlist():
#     global preferencesImportance
#     global dictionaryPreferences
#     df = initialize(dictionaryPreferences)
#     global top
#     top, refreshed, mList = movieList(df, preferencesImportance, dictionaryPreferences)
#     return top, refreshed, mList

# def saveTenMovies():
#     global dictionaryMovies
#     global top
#     listMovie = []
#     global string1
#     for index, row in top.iterrows():
#         dictionary = dict()
#         dictionary['title'] = row.primaryTitle
#         dictionary['year'] = row.startYear
#         dictionary['runtime'] = row.runtimeMinutes
#         dictionary['genres'] = row.genres
#         dictionary['rating'] = row.averageRating
#         dictionary['pplcategories'] = row.category
#         dictionary['pplnames'] = row.primaryName
#         dictionary['votes'] = row.numVotes
#         listMovie.append(dictionary)
#     return listMovie
        
# def returnStringText(self):
#     global top
#     global mList
#     listMovie = self.saveTenMovies()
#     string = ''
#     for i in range(len(listMovie)):
#         title = (".\nTitle: {}".format(listMovie[i]['title']))
#         string = string + str(i+1) + title + "\n"
#         string = string + listMovie[i]['summary']
#         runtime = "Runtime: {}\n".format(listMovie[i]['runtime'])
#         rating = "Rating: {} ({} votes)\n".format(listMovie[i]['rating'], listMovie[i]['votes'])
#         year = "Year of Release: {}\n".format(listMovie[i]['year'])
#         genre = ""
#         for j in range(len(listMovie[i]["genres"])):
#             if j != len(listMovie[i]["genres"])-1:
#                 genre = genre + listMovie[i]["genres"][j] + ", " 
#             else:
#                 genre = genre + listMovie[i]["genres"][j] + ""
#         genre = "Genre(s): {} \n".format(genre)
#         people = ""
#         eachperson = []
#         for p in range(len(listMovie[i]["pplcategories"])):
#             person = "   " + listMovie[i]["pplcategories"][p].title() + ": " + listMovie[i]["pplnames"][p] + "\n"
#             eachperson.append(person)
#         eachperson.sort(reverse=True)
#         for each in eachperson:
#             people = people + each 
#         people = "Film Crew:\n{}".format(people)
#         string = string + runtime + rating + year + genre + people
#         string = string + listMovie[i]['trailer'] + '\n'
#     return string

# global dictionaryPreferences
# dictionaryPreferences = {"valid": False, "maxtime": 180, "mintime":180, "genres":["Horror", "Comedy"], "minyear":1990, "maxyear": 2000, "maxrating":8.5, "minrating":8.4}
# global preferencesImportance
# preferencesImportance = {1:"Rating", 2:"Genres", 3:"Year", "valid":False}
# global top
# top, refresheddf, mList = returnTopRefreshedMlist()
# string = returnLabelText()
# print(string)
