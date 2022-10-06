import mysql.connector

# Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# Chequear la conexión
#print(database)

# Cursor que permite ejecutar las consultas
cursor = database.cursor()

# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
# Como crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id INT(10) AUTO_INCREMENT NOT NULL,
marca VARCHAR(40) NOT NULL,
modelo VARCHAR(40) NOT NULL,
precio FLOAT(10,2) NOT NULL,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
"""
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18123)")
coches = [
    ('Seat', 'Ibiza', 15456),
    ('Ford', 'Focus', 14556),
    ('Honda', 'Civic', 14563),
    ('Jeep', 'Willys', 4564)
]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches) # %s es una variable que permite sustituir por otros datos 

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 15000 AND marca = 'Jeep'")

result = cursor.fetchall() # fetchall() (saca todos los datos)

print("Todos los vehículos:")
for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone() # fetchone() (saca solo un valor)
print(coche)

