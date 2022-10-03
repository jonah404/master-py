# sqlite viene integrado con python.
# Importar módulo
import sqlite3

# Conexión a sqlite
conexion = sqlite3.connect("pruebas.db") #Crea el archivo

# Crear cursor (el cursor es el que permite ejecutar las consultas SQL)
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255)
);
""")


# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Descripcion del producto', 23)")
conexion.commit()
"""

# Borrar registros
#cursor.execute("DELETE FROM productos")
#conexion.commit()

# Insertar muchos registros de una
productos = [ 
    ("Ordenador", "Buen pc", 700),
    ("Telefono", "Buen telefono", 450),
    ("Placa", "Buena placa", 500),
    ("Tablet", "Buena tablet", 600),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)# executemany ejecuta varias consultas, con el signo "?" asigna los valores
conexion.commit()

# Update, actualizar datos
cursor.execute("UPDATE productos SET precio = 555 WHERE precio = 500")

# Lectura de datos de una tabla (listar datos)
cursor.execute("SELECT * FROM productos WHERE precio >= 500")
print(cursor)

productos = cursor.fetchall() #Trae todos los datos creados

for producto in productos:
    print("id: ", producto[0])
    print("Título: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone() #Saca el primer producto creado
print(producto)

# Cerrar conexión (sino el fichero queda abierto y los cambios no se guardan)
conexion.close()


