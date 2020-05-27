# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:57:21 2020

@author: NK
"""
import pandas as pd
data = pd.read_csv("datagg.csv", index_col = 0)
df = pd.DataFrame(data)
def sorted_age_list(df):
    sorted_list = []
    for row in df.itertuples():
        sorted_list.append(row[2])
    sorted_list.sort()
    return sorted_list
def age_descending_df(df):
    list_name = []
    df_copy = df.copy()
    index = 0
    for age in sorted_age_list(df)[::-1]:
        verbose = True
        for row in df.itertuples():
            if row[2] == age and verbose and row[1] not in list_name:
                df_copy.Name[index] = row[1]
                df_copy.Age[index] = age
                df_copy.Rating[index] = row[3]
                verbose = False
                list_name.append(row[1])
        index += 1       
    return df_copy