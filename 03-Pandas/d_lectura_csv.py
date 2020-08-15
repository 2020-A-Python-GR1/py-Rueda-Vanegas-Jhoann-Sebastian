# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:39 2020

@author: CAMILO
"""


#d_lectura_csv.py
import pandas as pd
import numpy as np

path = 'C://Users//CAMILO//Desktop//sebas//Universidad//semestre 2020-A//Python//py-Rueda-Vanegas-Jhoann-Sebastian//03-Pandas//data//artwork_data.csv'

df1 = pd.read_csv(
    path,nrows = 10)

columnas = ['id', 'artist', 'title',
            'medium', 'year',
            'acquisitionYear','height',
            'width','units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols=columnas)

df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')

path_guardado = 'C://Users//CAMILO//Desktop//sebas//Universidad//semestre 2020-A//Python//py-Rueda-Vanegas-Jhoann-Sebastian//03-Pandas//data//artwork_data.pickle'

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)




mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
df1 = pd.DataFrame(ser)