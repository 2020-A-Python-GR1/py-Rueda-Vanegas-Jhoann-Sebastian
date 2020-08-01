import numpy as np
import scipy.ndimage as ndimage
import scipy.misc as misc
import matplotlib.pyplot as plt
import random
from IPython.display import clear_output
from docutils.nodes import contact


class Imagen():


    def __init__(self, cortes):
        self.imagen = np.array(misc.ascent())
        self.mostrar_imagen_original()
        self.cortes_imagen = [] #tipo list
        self.cortar_imagen()
        self.imagen_original_array = np.array(self.cortes_imagen) #convierto en np array
        self.imagen_auxiliar = np.copy(self.imagen_original_array)
        self.imagen_auxiliar[0,0]= np.zeros_like(self.imagen_auxiliar[0,0])     #lleno primer elemento siempre de ceros,
                                                                                #a partir de aqui esta ordenada, pero con la primera posición de la matriz
                                                                                #llena de ceros, con esta voy a comparar cuando esté ordenada.

        self.lista_imagen = np.copy(self.imagen_auxiliar) #este es el array con el que voy a trabajar para mover las fichas
        self.array_ceros = [0,0]
        self.reordenar_imagen()
        self.mostrar_imagen_desordenada()
        self.iniciar_juego()


    def mostrar_imagen_original(self):
        plt.imshow(self.imagen)
        plt.show()

    def cortar_imagen(self):
        print('estoy en corte imagenes')
        corte_uno = np.vsplit(self.imagen, cortes)
        for i in range(cortes):
            self.cortes_imagen.append(np.hsplit(corte_uno[i], cortes))

    def reordenar_imagen(self):
        print("estoy en inicio reordenar")                      #entra con el shape(2,2,256,256) el array lista_imagen
        elemetos_h = random.sample(range(cortes), cortes)

        contador_filas = 0
        contardo_columnas = 0

        self.maux = np.zeros_like(self.lista_imagen)
        for j in elemetos_h:
            contardo_columnas = 0
            elemetos_v = random.sample(range(cortes),cortes)
            for i in elemetos_v:
                if(j==0 and i == 0):
                    self.array_ceros = [contador_filas,contardo_columnas]
                self.maux[contador_filas,contardo_columnas ,:,:] = np.array(self.lista_imagen[j,i,:,:])      #hasta aqui va quedar en el formato
                contardo_columnas +=1
            contador_filas += 1                                                                         #(n,n,:,:) n es el numero de cortes, y : es el restante para completar el size de la imagen


    def mostrar_imagen_desordenada(self):
        imagen_desordenada = []
        for i in range(cortes):
            imagen_desordenada.append(np.hstack(self.maux[i, :, :, :]))
        aux = np.vstack(imagen_desordenada)
        plt.imshow(aux)
        plt.show()


    def iniciar_juego(self):
        while(True):
            clear_output()
            self.comprobar_completado()
            ingreso = input("mueva las piezas segun corresponda: w(up), s(down), a(left), d(right), z(quit): ")
            if(ingreso == 'a'): #movimiento a la izquierda
                if(self.array_ceros[1] != 0): #toma la pieza y verifica si se puede mover en esa direccion
                    imagen_desordenada = np.copy(self.maux[self.array_ceros[0],self.array_ceros[1]-1])
                    self.maux[self.array_ceros[0],self.array_ceros[1]-1] = self.maux[self.array_ceros[0],self.array_ceros[1]]
                    self.maux[self.array_ceros[0],self.array_ceros[1]] = np.copy(imagen_desordenada)
                    self.array_ceros[1] = self.array_ceros[1] - 1
                else:
                    print("No se puede mover en esa direccion")
            if(ingreso == 'w'): #movimiento Arriba
                if(self.array_ceros[0] != 0):
                    imagen_desordenada = np.copy(self.maux[self.array_ceros[0]-1, self.array_ceros[1]])
                    self.maux[self.array_ceros[0] - 1, self.array_ceros[1]] = self.maux[self.array_ceros[0], self.array_ceros[1]]
                    self.maux[self.array_ceros[0], self.array_ceros[1]] = np.copy(imagen_desordenada)
                    self.array_ceros[0] = self.array_ceros[0] -1
                else:
                    print("no se puede mover en esa direccion")
            if(ingreso == 's'): #movimiento Abajo
                if(self.array_ceros[0] != cortes-1):
                    imagen_desordenada = np.copy(self.maux[self.array_ceros[0] + 1, self.array_ceros[1]])
                    self.maux[self.array_ceros[0] + 1, self.array_ceros[1]] = self.maux[self.array_ceros[0], self.array_ceros[1]]
                    self.maux[self.array_ceros[0], self.array_ceros[1]] = np.copy(imagen_desordenada)
                    self.array_ceros[0] = self.array_ceros[0] + 1
                else:
                    print("no se puede mover en esa direccion")
            if(ingreso == 'd'): #movimiento a la derecha
                if(self.array_ceros[1] != cortes-1):
                    imagen_desordenada = np.copy(self.maux[self.array_ceros[0], self.array_ceros[1] + 1])
                    self.maux[self.array_ceros[0], self.array_ceros[1] + 1] = self.maux[self.array_ceros[0], self.array_ceros[1]]
                    self.maux[self.array_ceros[0], self.array_ceros[1]] = np.copy(imagen_desordenada)
                    self.array_ceros[1] = self.array_ceros[1] + 1
                else:
                    print("No se puede mover en esa direccion")
            if(ingreso == 'z'):
                exit()
            self.mostrar_imagen_desordenada()
        clear_output()


    def comprobar_completado(self):
        if np.array_equal(self.imagen_auxiliar, self.maux):
            input("Felicidades, el juego ha terminado")


cortes = int(input("Ingresa el numero: "))
Imagen(cortes)

