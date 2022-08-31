# Tipos de datos.

nada             = None 
cadena           = "Hola soy Jona"
entero           = 66
flotante         = 6.5
booleano         = True
lista            = [10, 20, 30, 100] # La lista puede mezclar tipos de datos
tuplaNoCambia    = ("Master", "en", "Python")
diccionario      = {
    "nombre"  : "Jona",
    "apellido": "Alvarez"
}
rango            = range(9)
dato_byte        = b"Probando" #Poniendo la b adelante se indica es es un tipo de dato byte

# Mostrartipo de dato.

print(type(dato_byte))

# Convertir tipos de datos

texto = "Hola soy un texto"
num   = str(45) #float int
print(texto + " " + num)


