"""
Ejercicio 5:
Crear unaa lista con el contenido de esta tabla:
Accion Aventura Deportes
GTA    ASSASSIN FIFA
COD    CRASH    PRO22
PUBG   PRINCE   MOTOGP

Mostrar esta informacion ordenada
primero accion despues aventura y despues deportes

"""
tabla = [
    {
        "Categoría": "ACCION",
        "Juegos": ["GTA", "COD", "PUBG"]
    },
    {
        "Categoría": "AVENTURA",
        "Juegos": ["ASSASSIN", "CRASH", "PRINCE"]
    },
    {
        "Categoría": "DEPORTES",
        "Juegos": ["FIFA", "PRO22", "MOTOGP"]
    }
]


for categoria in tabla:
    print(f"----------{categoria['Categoría']}----------")
    for juego in categoria['Juegos']:
        print(juego)