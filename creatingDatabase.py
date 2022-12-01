# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:52:08 2022

@author: kelly
"""
import pandas as pd
import csv
 
# First section
basics = pd.read_csv(r'imdb\basics\data.tsv', sep='\t', header=0, low_memory = False)

ratings = pd.read_csv(r'imdb\rating\data.tsv',sep='\t', header=0, low_memory = False)

basics = basics.astype(str)
ratings = ratings.astype(str)

basics = basics.drop(['originalTitle','isAdult','endYear'], axis=1)

basics = basics.loc[(basics["runtimeMinutes"] != '\\N' )]
basics = basics.loc[basics['runtimeMinutes'].str.len() < 6]

ratings['numVotes'] = pd.to_numeric(ratings['numVotes'])
ratings = ratings.loc[(ratings["numVotes"].astype(int) >= 10000 )]

df = basics.merge(ratings, left_on='tconst', right_on='tconst')

df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes']) 

df = df.loc[(df["titleType"] == 'movie' )]

df.to_csv("db1.csv")

# Second Section

principals = pd.read_csv(r'imdb\title.principals.tsv\data.tsv', sep='\t', header=0, low_memory = False)

names = pd.read_csv(r'imdb\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

people = df.merge(principals, left_on='tconst', right_on='tconst')

people = people.merge(names, left_on="nconst", right_on='nconst')

people.to_csv('df2.csv') # created to be able to run script in sections

## Third Section
df = pd.read_csv('db1.csv', sep=',', header=0, low_memory = False)

df2 = pd.read_csv('db2.csv', sep=',', header=0, low_memory = False)

df2 = df2.drop(['birthYear', 'deathYear', 'primaryProfession', 'job', 'characters', 'ordering', 'knownForTitles'], axis=1)

df2 = df2.loc[(df2["category"] == 'actor' )|(df2["category"] == 'actress' )|(df2["category"] == 'director' )]

df2 = df2.sort_values(by="tconst")

category = df2['category'].groupby([df2.tconst]).apply(list).reset_index()
nconstants = df2['nconst'].groupby([df2.tconst]).apply(list).reset_index()
actornames = df2['primaryName'].groupby([df2.tconst]).apply(list).reset_index()

df2 = df2.drop_duplicates()

eachMovie = df.merge(category, left_on='tconst', right_on='tconst')
eachMovie = eachMovie.merge(actornames, left_on='tconst', right_on='tconst')
eachMovie = eachMovie.merge(nconstants, left_on='tconst', right_on='tconst')

eachMovie = eachMovie.drop(["Unnamed: 0"], axis=1)

eachMovie.to_csv('db3.csv')
