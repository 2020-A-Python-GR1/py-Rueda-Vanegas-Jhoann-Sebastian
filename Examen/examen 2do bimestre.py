# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from datetime import date


'''ejercicio uno'''
arr = np.random.randint(0,10,60).reshape(10,6)
df = pd.DataFrame(arr)


#primero 5 registros
df2 = df[0:5]
#últimos 5 registros
df3 = df[-5:]

'''ejercicio dos'''

arry = np.random.randint(0,20,24).reshape(6,4)

df4 = pd.DataFrame(arry,
                  index = [date.today(),date.today(),date.today(),date.today(),date.today(),date.today()],
                  columns = ['A','B','C','D']
                  )

'''ejercicio cuatro'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

#columnas
print(df5.columns.values)
#valores
print(df5.values)

'''ejercicio cinco'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

print(df5.describe())

'''ejercicio seis'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

print('dataframe transpuesto')
print(df5.transpose())

'''ejericio siete'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

for i in df5:
    print(df5[i].sort_values())
for j in df5:
    print(df5[j].sort_values(ascending= False))

'''ejercicio ocho'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

df6 = df5.where(df5.values > 7)


'''ejercicio nueve'''

df7 = df6.fillna(0)

'''ejercicio diez'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

print('promedio',np.average(df5))
print('media',np.mean(df5))
print('mediana',np.median(df5))

'''ejercicio once'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)
arr1 = np.random.randint(0,10,60).reshape(10,6)
df6 = pd.DataFrame(arr1)

df7 = df5.append(df6)

'''ejericio doce'''


arreglo = np.random.choice(['a','b','c','d','e','f','g','h','i','j'],60).reshape(10,6)
df11 = pd.DataFrame(arreglo)

df11['columna 1 y 2'] = df11[0] + "," + df11[1]
df11['columna 3 y 4'] = df11[2] + "," + df11[3]
df11['columna 5 y 6'] = df11[4] + "," + df11[5]


'''ejercicio 13'''

arr = np.random.randint(0,10,60).reshape(10,6)
df5 = pd.DataFrame(arr)

for i in df5:
    print(df5[i].value_counts())

'''ejercicio 14'''

arr = np.random.randint(0,10,30).reshape(10,3)
df10 = pd.DataFrame(arr, columns=['A','B','C'])

df10['D'] = (df10['A']*df10['B'])/(df10['C'])






















































