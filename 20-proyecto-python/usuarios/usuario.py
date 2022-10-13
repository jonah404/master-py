import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python",
    port=3306
)

cursor = database.cursor(buffered=True)

class Usuario:

    def __init__(self, nombre, apellido, email, passwd):
        self.nombre   = nombre
        self.apellido = apellido
        self.email    = email
        self.passwd   = passwd

    def registrar(self):
        fecha = datetime.datetime.now()

        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, self.passwd, fecha)

        cursor.execute(sql, usuario)
        database.commit()

        return[cursor.rowcount, self]

    def identificar(self):
        return self.nombre

