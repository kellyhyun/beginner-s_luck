# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:58:26 2022

@author: kelly
"""
import pandas as pd

df = pd.read_csv('FinalDatabase.csv', sep=',', header=0, low_memory = False)


genre = df.genres.unique()
uniqueList = []
for line in genre:
    x = line.split(",")
    for i in x:
        if not(i in uniqueList) and i not in ["Film-Noir", "\\N", "Short"]:
            uniqueList.append(i)
uniqueList.sort()
print(len(uniqueList))
for i in uniqueList:
    print(i)