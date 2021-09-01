"""
Proyecto de python y mysql
 -abrir asistente
 -login y registro
 -Si elegimod registro, creara un usuario en la bbdd
 -si elegimoos login, indentificate al usuario y nos preguntara
 -crear nota, mostrar notas, borrar nota.

"""
from usuarios import acciones# imortar modulo 
hazEl = acciones.Acciones()


print("""
ACCIONES Disponibles:
      
      -registro
      -login

""")



accion = input("Que quieres hacer: ")

if accion == "registro":
    hazEl.registro()
   
elif accion == "login":
    hazEl.login()
   
