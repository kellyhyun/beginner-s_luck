# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:58:32 2022

@author: kelly
"""
import pandas as pd
import csv
from pathlib import Path 



df = pd.read_csv('database3.csv', sep=',', header=0, low_memory = False)

df = df.drop(['birthYear', 'deathYear', 'primaryProfession', 'job', 'characters', 'directors', 'writers', 'Unnamed: 0.1','Unnamed: 0', 'isAdult', 'endYear', 'ordering', 'knownForTitles'], axis=1)

df = df.loc[(df["category"] == 'actor' )|(df["category"] == 'actress' )|(df["category"] == 'director' )]

df = df.sort_values(by="tconst")

category = df['category'].groupby([df.tconst]).apply(list).reset_index()
nconstants = df['nconst'].groupby([df.tconst]).apply(list).reset_index()
actornames = df['primaryName'].groupby([df.tconst]).apply(list).reset_index()


df = df.drop_duplicates()

eachMovie = pd.read_csv('ourDatabase.csv', sep=',', header=0, low_memory = False)

eachMovie = eachMovie.merge(category, left_on='tconst', right_on='tconst')
eachMovie = eachMovie.merge(actornames, left_on='tconst', right_on='tconst')
eachMovie = eachMovie.merge(nconstants, left_on='tconst', right_on='tconst')

eachMovie = eachMovie.drop(['isAdult', 'endYear'], axis=1)

df.to_csv('FinalDatabase.csv')

# birthYear	deathYear	primaryProfession
# job	characters
# directors	writers



