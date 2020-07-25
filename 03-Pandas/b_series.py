# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:51 2020

@author: CAMILO
"""

#b_series.py
# series es para 


import pandas as pd #sirve para analizar datos
import numpy as np

lista_numeros = [1,2,3,4]
tupla_numeros  = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)
series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Sebas",
    None,
    (1),
    [2],
    {"nombre":"Sebas"}
    ])

print(series_d[3])

lista_cuidades = ['Ambato', 'Cuenca', 'Loja','Quito']

series_cuidad = pd.Series(lista_cuidades,index=[
    "A","C","L","Q"])

print(series_cuidad[3])
print(series_cuidad["C"])

valores_ciudad = {"ibarra":9500,
                  "Guayaquil":10000,
                  "Cuenca":7000,
                  "Quito":8000,
                  "Loja":3000}

serie_valor_ciudad = pd.Series(valores_ciudad)

ciudades_menor_5k = serie_valor_ciudad < 5000

print(ciudades_menor_5k)
print(type(serie_valor_ciudad))             #<class 'pandas.core.series.Series'>
print(type(ciudades_menor_5k))              #<class 'pandas.core.series.Series'>

s5 = serie_valor_ciudad[ciudades_menor_5k]
serie_valor_ciudad = serie_valor_ciudad *1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

