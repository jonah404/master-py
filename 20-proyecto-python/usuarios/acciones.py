import usuarios.usuario as user

class Acciones:
    def registro(self):
        print("\nOk, vamos a registrarte en el sistema...")

        nombre   = input("¿Cuál es tu nombre? ")
        apellido = input("¿Cuál es tu apellido? ")
        email     = input("Ingresa tu email: ")
        passwd   = input("Ingresa una contraseña para acceder: ")

        usuario = user.Usuario(nombre, apellido, email, passwd)
        registro = usuario.registrar()

        if registro[0]>=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado en el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
    
    def login(self):
        print("\nPor favor identifícate en el sistema...")

        email   = input("Ingresa tu email: ")
        passwd = input("Ingresa la contraseña: ")