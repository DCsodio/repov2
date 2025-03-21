import funciones_inicio
import funciones_login
import func_aux
import time #agregar delay
import os #limpiar terminal

"""
perfiles=[
    {
        "usuario":"DCsodio",
        "contrasenia":"123456"
    },
    {
        "usuario":"caro1234",
        "contrasenia":"123456"
    }
]
"""
perfiles=[]
usuario=""
clave=""
opcion=1

while opcion!=0:
    opcion=funciones_inicio.menu_inicio()
    if opcion==0:
        print("Selecciono salir")
    elif opcion==1:
        print("Selecciono la opcion crear perfil")
        funciones_inicio.crear_perfil(perfiles)
    elif opcion==2:
        print("Selecciono mostrar perfiles")
        funciones_inicio.mostrar_perfiles(perfiles)
    elif opcion==3:
        print("Selecciono login")
        usuario,clave=func_aux.ingreso_id()
        id_correcto=funciones_inicio.login(perfiles,usuario,clave)
        if id_correcto:
            funciones_login.menu_usuario(perfiles,usuario,clave)


    print("espere...")
    time.sleep(3)
    os.system("clear")

print("-adios-")