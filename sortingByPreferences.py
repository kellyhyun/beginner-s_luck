# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:34:22 2022

@author: kelly
"""
import pandas as pd

basics = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\ourDatabase.csv', sep=',', header=0, low_memory = False)

basics['runtimeMinutes'] = pd.to_numeric(basics['runtimeMinutes'])
basics['numVotes'] = pd.to_numeric(basics['numVotes'])

# finding movies with runtime between 115 and 120
df = basics.loc[(basics['runtimeMinutes']<=120) & (basics['runtimeMinutes']>=115)]

# sorting with numVotes as top priority, avg rating as 2nd priority
df = df.sort_values(by=['numVotes', 'averageRating'])

# finding all movies with horror genre as well - doing priority for this would need more thought
df['genres'] = df['genres'].str.lower()
df = df.loc[df['genres'].str.contains('horror')]


dfBest = df.head(10)
dfWorst = df.tail(10)
    
print(dfBest)
print(dfWorst)
