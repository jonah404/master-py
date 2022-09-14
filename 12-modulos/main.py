"""
Un módulo son funcionalidades ya hechas para reutilizar.
Consulta de modulos:
https://docs.python.org/3/py-modindex.html

Podemos conseguir móduclos que ya vienen el el lenguaje,
se pueden conseguir en internet y también podemos crear modulos propios
"""

# Importar modulo propio, se llama directamente al archivo o nombre del módulo 
#import mimodulo #De esta forma se importa el modulo completo
#from mimodulo import holaMundo #De esta forma se importa solo la función "holaMundo" del modulo
from mimodulo import *

#print(mimodulo.holaMundo("Jonatan"))
#print(mimodulo.calculadora(2,5,False))
print(holaMundo("Jonatan"))
print(calculadora(1,2,True))

# Modulo fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.minute)
print(fecha_completa.month)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)


print(datetime.datetime.now().timestamp())

# Modulo matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", math.pi)
print("Redondear: ", math.ceil(6.456163521651)) #Redondea para arriba, con .floor para abajo

#Modulo random
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))