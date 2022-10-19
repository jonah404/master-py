import usuarios.usuario as user
import notas.acciones

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

        try:
            email   = input("Ingresa tu email: ")
            passwd = input("Ingresa la contraseña: ")

            usuario = user.Usuario('','', email, passwd)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}.")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto, intenta más tarde")
    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto.")
            exit()

