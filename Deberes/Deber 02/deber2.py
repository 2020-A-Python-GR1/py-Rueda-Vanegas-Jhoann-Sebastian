import numpy as np
import scipy.ndimage as ndimage
import scipy.misc as misc
import matplotlib.pyplot as plt
from PIL import Image

path = "./imagen.jpeg"
imagen = Image.open(path,"r")

plt.imshow(imagen)
plt.show()
#imagen.shape

imagen_array = np.array(imagen)
imagen_array.shape
print(imagen_array.shape)
#512,512
plt.imshow(imagen)

print(imagen_array)

corte_uno,corte_dos= np.split(imagen_array,2)   #c1,c2,c3,c4 = np.split(imagen_array.flatten(),4)
plt.imshow(corte_uno)                           #c1.shape
c1,c2 = np.hsplit(corte_uno,2)                  #c1.reshape(256,256)
c3,c4 = np.hsplit(corte_dos,2)                  #c2.reshape(256,256)
plt.imshow(c4)                                  #c3.reshape(256,256) #c4.reshape(256,256)


#plt.imshow(c1.reshape(256,256))
print(c4.shape)                                        #cuadro_dos = np.hsplit(corte_v1,2)
                                                #cuadro_tres,cuadro_cuatro = np.hsplit(corte_v2,2)

imagen_completa = [c1,c2,c3,c4]

mitad1 = np.array(imagen_completa[0,1])
mitad2 = np.array(imagen_completa[2,3])

m1 = np.concatenate(mitad1,axis = 1)
m2 = np.concatenate(mitad2,axis = 1)

plt.imshow(np.concatenate([m1,m2]))



