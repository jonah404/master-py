# Definir las funciones en la parte superior del archivo.
# Lo recomendable es que una función devuelva un dato (return)
# Se puede acceder a las variables locales desde las funciones.
# Se recomienda (aa menos que sean datos concretos) pasar los datos de las variables como parametros de la función.

def mi_funcion(nombre):
    return "Hola que tal " + nombre

def otra_funcion(apellido):
    return "Hola que tal 2 " + apellido

nombre = "Jona"
apellido = "Alva"
#La llamada a la función va despues de definir las variables.
print(mi_funcion(nombre))
print(otra_funcion(apellido))

