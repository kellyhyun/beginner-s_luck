# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:06:39 2022

@author: 12818
"""

import pandas as pd
import csv
from pathlib import Path 
import numpy as np


basics = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\basics\data.tsv', sep='\t', header=0, low_memory = False)

ratings = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\rating\data.tsv',sep='\t', header=0, low_memory = False)

basics = basics.astype(str)
ratings = ratings.astype(str)

basics = basics.loc[(basics["runtimeMinutes"] != '\\N' )]
basics = basics.loc[basics['runtimeMinutes'].str.len() < 6]

ratings['numVotes'] = pd.to_numeric(ratings['numVotes'])
ratings = ratings.loc[(ratings["numVotes"].astype(int) >= 10000 )]

basics = basics.merge(ratings, left_on='tconst', right_on='tconst')

# print(basics)

df = pd.read_csv('ourDatabase.csv', sep=',', header=0, low_memory = False)

crew = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\title.crew.tsv\data.tsv', sep='\t', header=0, low_memory = False)

principals = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\title.principals.tsv\data.tsv', sep='\t', header=0, low_memory = False)

names = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

# newDF
df_names = df.merge(crew, left_on='tconst', right_on='tconst')

# newnewDF
df_names_principals = df_names.merge(principals, left_on='tconst', right_on='tconst')

# newDF = df.merge(crew, left_on='tconst', right_on='tconst')

# newnewDF = newDF.merge(principals, left_on='tconst', right_on='tconst')

# newnewDF.to_csv('database2.csv') 

# df = pd.read_csv('database2.csv', sep=',', header=0, low_memory = False)

# names = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

# newDF = df.merge(names, left_on='nconst', right_on='nconst')


filepath = Path(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\database3.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  

df_names_principals.to_csv(filepath)
# newDF.to_csv(filepath) 


''''' below is pythontest, addingpeopletodatabase, and addingnamestodata
copy pasted one after the other, the above part is them copy pasted, but i tried
to reduce the redundancies '''''


# basics = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\basics\data.tsv', sep='\t', header=0, low_memory = False)

# ratings = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\rating\data.tsv',sep='\t', header=0, low_memory = False)

# basics = basics.astype(str)
# ratings = ratings.astype(str)

# basics = basics.loc[(basics["runtimeMinutes"] != '\\N' )]
# basics = basics.loc[basics['runtimeMinutes'].str.len() < 6]

# ratings['numVotes'] = pd.to_numeric(ratings['numVotes'])
# ratings = ratings.loc[(ratings["numVotes"].astype(int) >= 10000 )]

# basics = basics.merge(ratings, left_on='tconst', right_on='tconst')

# print(basics)

# df = pd.read_csv('ourDatabase.csv', sep=',', header=0, low_memory = False)

# crew = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\title.crew.tsv\data.tsv', sep='\t', header=0, low_memory = False)

# principals = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\title.principals.tsv\data.tsv', sep='\t', header=0, low_memory = False)

# names = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

# newDF = df.merge(crew, left_on='tconst', right_on='tconst')

# newnewDF = newDF.merge(principals, left_on='tconst', right_on='tconst')

# newnewDF.to_csv('database2.csv') 

# df = pd.read_csv('database2.csv', sep=',', header=0, low_memory = False)

# names = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

# newDF = df.merge(names, left_on='nconst', right_on='nconst')

# filepath = Path(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\database3.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# newDF.to_csv(filepath) 