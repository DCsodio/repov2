import funciones_inicio
import func_aux

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
    if opcion==1:
        print("Selecciono la opcion crear perfil")
        funciones_inicio.crear_perfil(perfiles)
    elif opcion==2:
        funciones_inicio.mostrar_perfiles(perfiles)
print("-adios-")