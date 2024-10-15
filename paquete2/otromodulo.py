'''

Podemos importar la clase de las 2 maneras
1. En la primera tenemos que poner el nombre de la clase más la funcion
2. en la segunda ponemos solo el nombre de la funcion
3. en la ultima importamos todo
'''
from paquete1 import modulo
from paquete1.modulo import mi_funcion
from paquete2.paquetehijo2.modulopaquetehijo3 import otra_funcion
from paquetehijo2 import *
#from modulo import *

if __name__ == '__main__':
    modulo.mi_funcion()
    mi_funcion()

otra_funcion()