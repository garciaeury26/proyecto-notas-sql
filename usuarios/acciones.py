import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nok!! vamos a registrarte en el sistema")

        nombre = input("Cual es tu nombre: ")
        apellidos = input("Dame un apellidos: ")
        email = input("Escribe tu imail: ")
        password = input("Escribe tu contra: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nperfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nRegistro incorrecto")
    
    def login(self):
        print("\nvale identificate en el sistema")
        
        try:
            email = input("Escribe tu imail: ")
            password = input("Escribe tu contra: ")

            usurio = modelo.Usuario('','',email, password)
            login = usurio.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el siste ma el dia {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto")    

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles"
              -crear nota(crear)
              - mostrar tus notas(mostrar)
              -eliminar notas(eliminar)
              -salir (salir)
        """)

        accion = input("Que quieres hacer: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)


        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Ok nos vemos {usuario[1]}")
            exit()


        return None



     