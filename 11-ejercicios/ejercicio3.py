"""
Ejercicio 3
Crear un programa que compruebe si una variable esta vacía
y si esta vacía rellenarla con texto en minúuculas y luego 
mostrarlo en mayúsculas.

"""

texto = ""

if len(texto.strip()) <= 0: #comprueba la extensión del texto "len" y .strip elimina los espacios en blanco
    texto = "Hola soy un texto"
    print(texto.upper()) #.upper muestra texto en mayúsculs, lower en minusculas
else:
    print(f"la variable tiene contenido: {texto}")




