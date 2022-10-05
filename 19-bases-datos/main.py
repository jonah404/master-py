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

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)