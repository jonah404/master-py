"""
Diccionario:
Es un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.

"""
# Creación de un diccionario
persona = {
    "nombre": "Jonatan",
    "apellido": "Alvarez",
    "web:": "jona.com"
}

print(persona["nombre"])

# Lista con diccionarios, creacion de una lista con diccionarios

contactos = [
    {
        'nombre': 'jonatan',
        'email': 'jona@mail.com'
    },
    {
        'nombre': 'paula',
        'email': 'paula@mail.com'
    },
    {
        'nombre': 'vanesa',
        'email': 'vane@mail.com'
    }
]

contactos[0]['nombre'] = "Jona" #Modificar el valor de un dato dentro del diccionrio

print(contactos[0]['nombre'])

print("\nLista de contactos:")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")