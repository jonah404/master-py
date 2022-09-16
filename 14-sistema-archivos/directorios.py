import os #Para trabajar con directorios
import shutil #para copiar archivos y renombrar

# Crear carpeta

if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):# Busca si existe la carpeta en el directorio
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("El directorio ya existe")



#Copiar una carpeta
"""
ruta_original =  "./14-sistema-archivos/mi_carpeta"
ruta_nueva =  "./14-sistema-archivos/mi_carpeta_copiada"

shutil.copytree(ruta_original, ruta_nueva) #para realizar una copia de la carpeta (copyfile "archivos" - copytree "carpetas")
"""
# Eliminar una carpeta

#os.rmdir("./14-sistema-archivos/mi_carpeta_copiada")

# Listar archivos que hay dentro de la carpeta

print("Contenido de mi carpeta: ")
contenido = os.listdir("./14-sistema-archivos/mi_carpeta") #lista todos los archivos que hay dentro de la ruta especificada

for archivo in contenido:
    print("Archivo: "+ archivo)



