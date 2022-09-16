from io import open #para abrir archivo y crear
import pathlib #para escribir y leer contenido
import shutil #para copiar archivos y renombrar
import os #para eliminar archivos
import os.path #para comprobar si existen directorios/archivos

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir
archivo.write("******* Soy un texto metido desde python **********\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    #lista_frase = frase.split()
    #print(lista_frase)
    #print("- "+frase.upper())
    print("- "+frase.center(100))

# Copiar 
"""
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt" #cambio el nombre del archivo

shutil.copyfile(ruta_original, ruta_nueva) #para realizar una copia del archivo
"""
# Mover archivos
"""
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado_nuevo.txt" #cambio el nombre del archivo

shutil.move(ruta_original, ruta_nueva) # muevo el archivo a otra ubicacion
"""

#Eliminar archivos
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado_nuevo.txt"
os.remove(ruta_nueva) #para eliminar archivos
"""
#Comprobar si existe un archivo

#print(os.path.abspath("../")) #Muestra la ruta absoluta

comprobar_ruta = os.path.abspath("./") + "/14-sistema-archivos/fichero_texto.txt" #muestra ruta
print(comprobar_ruta)

if os.path.isfile(comprobar_ruta): #comprueba si el archivo existe
    print("El archivo existe")
else:
    print("El archivo no existe")




