# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:52:08 2022

@author: kelly
"""
import pandas as pd
import csv
from pathlib import Path 
import numpy as np
 

# basics = dropped some columns - deleted the code oops - can find later
# https://www.shanelynn.ie/pandas-drop-delete-dataframe-rows-columns/ explains drop 
# basics = basics.loc[(basics["runtimeMinutes"] != '\\N' )]

# basics['runtimeMinutes'] = basics.runtimeMinutes.astype(str)

# basics = basics.loc[basics['runtimeMinutes'].str.len() < 6]

# basics['runtimeMinutes'] = pd.to_numeric(basics['runtimeMinutes'])




basics = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\basics\data.tsv', sep='\t', header=0, low_memory = False)

ratings = pd.read_csv(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\rating\data.tsv',sep='\t', header=0, low_memory = False)

basics = basics.astype(str)
ratings = ratings.astype(str)

basics = basics.loc[(basics["runtimeMinutes"] != '\\N' )]
basics = basics.loc[basics['runtimeMinutes'].str.len() < 6]

ratings['numVotes'] = pd.to_numeric(ratings['numVotes'])
ratings = ratings.loc[(ratings["numVotes"].astype(int) >= 10000 )]

basics = basics.merge(ratings, left_on='tconst', right_on='tconst')

print(basics)
# result = []

# for index, row in ratings.iterrows():
#     tConst = row["tconst"]
#     avgRating = row["averageRating"]
#     numVotes = row["numVotes"]
#     for value in basics["tconst"]:
#         if value == tConst:
#             print('equal!')
#             result.append(avgRating)
            
# basics["Result"] = result

# filepath = Path(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\ourDatabase.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# basics.to_csv(filepath) 

# basics['runtimeMinutes'] = pd.to_numeric(basics['runtimeMinutes']) - shows us to take out reality tv


    
    

# basics = basics.loc[(basics["runtimeMinutes"].astype(int) > 14 )] # data["runtimeMinutes"] & (data["deaths_24_hours"] > 0)


# CREATING NEW FILE
# filepath = Path(r'C:\Users\kelly\OneDrive\Documents\homework\!Fall 2023\ME396P-Proj\basics\dataShortened.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# basics.to_csv(filepath)  


