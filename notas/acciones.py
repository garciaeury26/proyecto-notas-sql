import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"ok{usuario[1]} vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("mete el conteido de tu nta: ")


        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nperfecto has guardao la nota: {nota.titulo}")
            
        else:
            print(f"No se ha guardado la nota {usuario[1]} ")


    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]} !! aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n******************")
            print(nota[2])
            print(nota[3])
            print("******************")
    
    def borrar(self, usuario):
        print(f"\n ok {usuario[1]}!! vamos a borrar notas")

        titulo = input("introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("nose ha borrado la nota")