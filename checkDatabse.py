# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:19:24 2022

@author: kelly
"""
import pandas as pd
import ast
import json

df = pd.read_csv('FinalDatabase.csv', sep=',', header=0, low_memory = False)

df["category"] = df["category"].str.replace("[' ]","")
df['category'] = df.category.apply(lambda x: x[1:-1].split(','))

df["nconst"] = df["nconst"].str.replace("[' ]","")
df['nconst'] = df.nconst.apply(lambda x: x[1:-1].split(','))

df["primaryName"] = df["primaryName"].str.replace("[' ]","")
df['primaryName'] = df.primaryName.apply(lambda x: x[1:-1].split(','))

for index, row in df.iterrows():
    catlist = row["category"]
    print(catlist)
    for i in catlist:
        print(i)
    print(row["nconst"], len(row["nconst"]))
    print(row["primaryName"], len(row["primaryName"]))
    assert(len(row["category"]) == len(row["nconst"]) != len(row["primaryName"]))