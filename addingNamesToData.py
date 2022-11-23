# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:58:32 2022

@author: kelly
"""
import pandas as pd
import csv
from pathlib import Path 



df = pd.read_csv('database2.csv', sep=',', header=0, low_memory = False)

names = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\name.basics.tsv\data.tsv', sep='\t', header=0, low_memory = False)

newDF = df.merge(names, left_on='nconst', right_on='nconst')

filepath = Path(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\database3.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
newDF.to_csv(filepath) 

