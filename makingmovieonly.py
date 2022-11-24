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

df = df.loc[(df["titleType"] == 'movie' )]
print(df.head())
df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)


df.to_csv('FinalDatabase-MovieOnly.csv')
