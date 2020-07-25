import numpy as np
import scipy.ndimage as ndimage
import scipy.misc as misc
import matplotlib.pyplot as plt
import random
from IPython.display import clear_output

class Imagen():

    imagen = None
    imagen_aux = None

    def __init__(self,imagen):
        self.imagen = imagen
        self.imagen_aux


    def mostrar_imagen(self, imagen):
        plt.imshow(imagen)
        plt.show()

    def reordenar_imagen(self,lista):
        array = np.zeros(65536).reshape(256, 256)
        lista[0] = array
        random.shuffle(lista, random.random)
        mitad1 = np.array([lista[0],lista[1]])
        mitad2 = np.array([lista[2],lista[3]])
        m1 = np.concatenate(mitad1,axis = 1)
        m2 = np.concatenate(mitad2,axis = 1)
        imagen_aux = np.concatenate([m1,m2])
        return ima3

    def cortar_imagen(self,imagen,cortes):                       #por ahora vamos a hacer de 2x2
        corte_uno,corte_dos= np.split(imagen,cortes)
        c1, c2 = np.hsplit(corte_uno, 2)
        c3, c4 = np.hsplit(corte_dos, 2)
        lista = [c1,c2,c3,c4]
        return lista

    def mover_piezas(self):
        while (1):
            clear_output()
            plt.pause(1)
            self.comprobar_completado()
            valor = input("←(a)  ↑(w)  →(d)   ↓(s)  q (salir)")
            if (valor == "a"):
                if (self.posicion_valor[1] != 0):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1] - 1])
                    self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1] - 1] = self.imagen_auxiliar[
                        self.posicion_valor[0], self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[1] = self.posicion_valor[1] - 1
                else:
                    print("no puede realizar esete movimiento")
            if (valor == "w"):
                if (self.posicion_valor[0] != 0):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0] - 1, self.posicion_valor[1]])
                    self.imagen_auxiliar[self.posicion_valor[0] - 1, self.posicion_valor[1]] = self.imagen_auxiliar[
                        self.posicion_valor[0], self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[0] = self.posicion_valor[0] - 1
                else:
                    print("no puede realizar esete movimiento")
            if (valor == "s"):
                if (self.posicion_valor[0] != self.dimenciones - 1):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0] + 1, self.posicion_valor[1]])
                    self.imagen_auxiliar[self.posicion_valor[0] + 1, self.posicion_valor[1]] = self.imagen_auxiliar[
                        self.posicion_valor[0], self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[0] = self.posicion_valor[0] + 1
                else:
                    print("no puede realizar esete movimiento")
            if (valor == "d"):
                if (self.posicion_valor[0] != self.dimenciones - 1):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1] + 1])
                    self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1] + 1] = self.imagen_auxiliar[
                        self.posicion_valor[0], self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0], self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[1] = self.posicion_valor[1] + 1
                else:
                    print("no puede realizar esete movimiento")
            if (valor == "q"):
                break
            self.imprimir_puzzle()
        clear_output()

    def comprobar_completado(self):
        if np.array_equal(self.imagen_aux, self.imagen):
            input("Felicidades, juego terminado")


imagen = misc.ascent()
plt.imshow(imagen)
plt.show()
im = Imagen(imagen)
lista = im.cortar_imagen(imagen,2)
imagen_reordenada = im.reordenar_imagen(lista)
plt.imshow(imagen_reordenada)
plt.show()
im.mover_piezas()