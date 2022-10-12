"""
Proyecto Python mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar nota, borrarlas (abm)
"""

from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "Registro":
    hazEl.registro()

elif accion == "Login":
    hazEl.login()

