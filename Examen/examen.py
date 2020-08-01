# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:09:26 2020

@author: Sebas
"""

import numpy as np
import pandas as pd
import random
import scipy.ndimage as ndimage
import scipy.misc as misc
import matplotlib.pyplot as plt


#llenar un array de 0s con tamaño n
arreglo = np.zeros(10)
print(arreglo)

#crear un arreglo y ponerle a la posisción 5 el valor de 1
arreglo[5] = 1
print(arreglo)

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

array = np.arange(50)
print(array[::-1])

## 5) Crear una matriz de 3 x 3 con valores del cero al 8

a2 = np.arange(9).reshape(3,3)

print(a2)

## 6) Encontrar los indices que no sean cero en un arreglo


arreglo = [1,2,0,0,4,0]
a3 = np.array(arreglo)

print(np.where(a3 == 0))

## 7) Crear una matriz de identidad 3 x 3 

a4 = np.identity(3)
print(a4)

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos
a5 = np.random.randint(0,20,27).reshape(3,3,3)
print(a5)

## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

c = np.random.randint(0,50,100).reshape(10,10)
print(c)
print("el valor menor es: ")
print(c.min())
print("el valor mayor es: ")
print(c.max())


## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)


mapache = misc.face()
print(mapache[::,3])
plt.imshow(mapache)
plt.show()


## 11) ¿Como crear una serie de una lista, diccionario o arreglo?


mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(myarr, mylist))


series_lista = pd.Series(mylist)
series_tupla = pd.Series(myarr)
series_diccionario = pd.Series(mydict)


## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(myarr, mylist))

ser = pd.Series(mydict) 
s1 = pd.Series(myarr)
s2 = pd.Series(mylist)
# Transformar la serie en dataframe y hacer una columna indice
df1 = pd.DataFrame()

df1[0] = s1
df1[1] = s2

df1.columns = ['Indice','letra']

## 13) ¿Como combinar varias series para hacer un DataFrame?

import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df2 = pd.DataFrame()
df2[0] = ser1
df2[1] = ser2

## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

items = ser1.isin(ser2)
items_negacion = ser1[~items]
print(items_negacion)

## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print(ser.value_counts())

## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?



np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
num_veces = ser.value_counts()
ser[ser.isin(ser.value_counts().index[:2])] = 0


## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?

ser = pd.Series(np.random.randint(1, 10, 35))
df3 = pd.DataFrame(np.array(ser).reshape(7,5))

## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?


ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u

ser2 = ser[pos]

print(ser2)

## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?


ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df4 = pd.DataFrame()
#las series son cloumnas en Dataframes, por eso solo puedo agregar series de manera vertical
#lo que podria hacer horizontalmente es agregar valores a cada una de las series que existen

#veritcalmente
df4[0] = ser1
df4[1] = ser2

#horizontalmente
df5 = pd.DataFrame()

df5 = df5.append(ser1, ignore_index=True)
df5 = df5.append(ser2,ignore_index=True)


## 21)¿Obtener la media de una serie agrupada por otra serie?

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
df = pd.DataFrame({'Frutas':frutas,
                   'Pesos':pesos})
df[0] = frutas
df[1] = pesos

print(df.groupby(['Frutas']).mean())


## 22)¿Como importar solo columnas especificas de un archivo csv?

path = "C://Users//CAMILO//Desktop//sebas//Universidad//semestre 2020-A//Python//py-Rueda-Vanegas-Jhoann-Sebastian//Examen//BostonHousing.csv"

columnas = ["crim","zn","indus","chas","nox"]
df1 = pd.read_csv(
    path,nrows = 20,
    usecols = columnas)



