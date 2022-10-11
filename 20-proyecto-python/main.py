"""
Proyecto Python mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar nota, borrarlas (abm)
"""

print("""
Acciones disponibles:
    - Registro
    - Login
""")

accion = input("¿Que quieres hacer?: ")

if accion == "Registro":
    print("\nOk, vamos a registrarte en el sistema...")

    nombre   = input("¿Cuál es tu nombre? ")
    apellido = input("¿Cuál es tu apellido? ")
    mail     = input("Ingresa tu email: ")
    passwd   = input("Ingresa una contraseña para acceder: ")

elif accion == "Login":
    print("Por favor identifícate en el sistema...")

    mail   = input("Ingresa tu email: ")
    passwd = input("Ingresa la contraseña: ")

