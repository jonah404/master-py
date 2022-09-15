from io import open #para abrir archivo y crear
import pathlib #para escribir y leer contenido
import shutil #para copiar archivos renombrar, eliminar.etc

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
ruta_original = ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
ruta_nueva = ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt" #cambio el nombre del archivo

shutil.copyfile(ruta_original, ruta_nueva) #para realizar una copia del archivo


