import func_aux
import funciones_inicio

def menu_usuario ():

    opcion=1
    while(opcion!=0):
        print("Se logueo correctamente")
        print("0- Salir")
        print("1- Ver listado de musica")
        print("2- Modificar perfil")
        print("3- Eliminar perfil")

        opcion =int(input("ingrese una opcion en forma de numero"))
        if(opcion==0):
            return print("adios")
        elif (opcion==1):
            return 0 #listado de musica
        elif (opcion==2):
            funciones_inicio.modificar_perfil()
        elif (opcion==3):
            funciones_inicio.eliminar_perfil()