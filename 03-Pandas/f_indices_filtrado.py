# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:12:22 2020

@author: Sebas
"""


import pandas as pd

path_pickle = r"C:\Users\CAMILO\Desktop\sebas\Universidad\semestre 2020-A\Python\py-Rueda-Vanegas-Jhoann-Sebastian\03-Pandas\data\artwork_data.pickle"

df = pd.read_pickle(path_pickle)

series_artistas_dup = df['artist']

artistas = pd.unique(series_artistas_dup)

print(type(artistas))  #numpy array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William'  #Serie

print(blake.value_counts())

df_blake = df[blake]  #dataframe

