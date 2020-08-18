# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:38 2020

@author: Sebas
"""

import pandas as pd

path_guardado = r"C:\Users\CAMILO\Desktop\sebas\Universidad\semestre 2020-A\Python\py-Rueda-Vanegas-Jhoann-Sebastian\03-Pandas\data\artwork_data.pickle"

df = pd.read_pickle(path_guardado)
#loc

filtrado_horizontal = df.loc[1035]
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index)   #indices son las columnas



serie_vertical = df['artist']            
print(serie_vertical)
print(serie_vertical.index)    #indices son los indices normales


#filtrado por indice

df_1032 = df[df.index == 1035]


#con loc accedemos a un grupo de filas y columnas x labels

segundo = df.loc[1035]   #filtrar por indice (1)
segundo = df.loc[[1035,1036]]  #filtrar por arr indices
segundo = df.loc[3:5]  #filtrado desde x indice hasta y indice
segundo = df_1032 = df[df.index == 1035] #filtrar x un arreglo de vdd y falses


segundo =df.loc[1035, 'artist']  #1 indice
segundo = df.loc[1035, ['artist', 'medium']]   #varios indices


#print(df.loc[0])  #indice  demtro dewl dataaframe, por eso da error


tercero = df.iloc[0]   #filtrar por indice (1)
tercero = df.iloc[[0,1]]  #filtrar por arr indices
tercero = df.iloc[0:10]  #filtrado desde x indice hasta y indice
tercero = df.iloc[df.index == 1035] #filtrar x un arreglo de vdd y falses

tercero = df.iloc[0:10, 0:4]   #filtrado por indices y por rango de indice 0:4


#######################################33

datos = {
    'nota 1':{
        'pepito':7,
        'juanita':8,
        'maria':9},
    'nota 2':{
        'pepito':7,
        'juanita':8,
        'maria':9},
    'disciplina':{
        'pepito':4,
        'juanita':9,
        'maria':2},
    }

notas = pd.DataFrame(datos)


condicion_nota = notas['nota 1'] > 7
condicion_nota2 = notas['nota 2'] > 7
condicion_disc = notas['disciplina'] > 7


mayores_siete = notas.loc[ condicion_nota,['nota 1']]

#esto funciona como un and para filtrar los datos
pasaron = notas.loc[condicion_nota][condicion_nota2][condicion_disc]

notas.loc['maria', 'disciplina'] = 7
notas.loc[:, 'disciplina'] = 7


####################################################################
##promedio de las 3 notas n1+n2+d / 3


promedio_notas = (notas.loc[:,'nota 1']+ notas.loc[:,'nota 2']+ notas.loc[:,'disciplina']) / 3








































