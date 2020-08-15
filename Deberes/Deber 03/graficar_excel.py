# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:44:47 2020

@author: CAMILO
"""


import pandas as pd
import numpy as np
import xlsxwriter

path_pickle = r"C:\Users\CAMILO\Desktop\sebas\Universidad\semestre 2020-A\Python\py-Rueda-Vanegas-Jhoann-Sebastian\03-Pandas\data\artwork_data.pickle"



df = pd.read_pickle(path_pickle)
sub_df = df.iloc[49980:50519,:].copy()


path_excel = r"C:\Users\CAMILO\Desktop\sebas\Universidad\semestre 2020-A\Python\py-Rueda-Vanegas-Jhoann-Sebastian\Deberes\Deber 03\artwork_data.xlsx"


numero_artistas = sub_df["artist"].value_counts()

workbook = xlsxwriter.Workbook(path_excel)

worksheet = workbook.add_worksheet()
worksheet.write_column('A1', 'Artist')
worksheet.write_column('B1', 'Valor')
worksheet.write_column('A2', numero_artistas.index)
worksheet.write_column('B2', numero_artistas.values)

chart = workbook.add_chart({'type':'pie'})
chart.add_series({'categories': '=Sheet1!$A$2:$A$85',
                  'values': '=Sheet1!$B$2:$B$85'
                  })

chart.set_title({'name':'Resultados'})

worksheet.insert_chart('D2', chart)

workbook.close()