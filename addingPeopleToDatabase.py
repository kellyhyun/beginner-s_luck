# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:58:32 2022

@author: kelly
"""
import pandas as pd
import csv
from pathlib import Path 



df = pd.read_csv('ourDatabase.csv', sep=',', header=0, low_memory = False)

crew = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\title.crew.tsv\data.tsv', sep='\t', header=0, low_memory = False)

principals = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\title.principals.tsv\data.tsv', sep='\t', header=0, low_memory = False)

names = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

newDF = df.merge(crew, left_on='tconst', right_on='tconst')

newnewDF = newDF.merge(principals, left_on='tconst', right_on='tconst')

filepath = Path(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\database2.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
newnewDF.to_csv(filepath) 

