import func_aux
import funciones_inicio
import os
import time

def menu_usuario (perfiles:list, usuario:str, clave:str):

    opcion=1
    while(opcion!=0):
        print("Se logueo correctamente")
        print("0- Salir")
        print("1- Ver listado de musica")
        print("2- Modificar usuario")
        print("3- Eliminar perfil")

        opcion =int(input("ingrese una opcion en forma de numero: "))
        if(opcion==0):
            return print("adios")
        elif (opcion==1):
            return 0 #listado de musica
        elif (opcion==2):
            print("--selecciono modificar usuario")
            modificar_usuario(perfiles,usuario)
        elif (opcion==3):
            funciones_inicio.eliminar_perfil()
        print("espere...")
        time.sleep(5)
        os.system("clear")

def modificar_usuario(perfiles:list, usuario:str):
    if not isinstance(usuario, str):    #proteccion
        raise TypeError("el argumento usuario debe ser str")
    """
        raise TypeError ("falla")  detiene el programa
        isistance (variable, formato) #si coincide manda true 
    """
    if not isinstance(perfiles,list): #proteccion
        raise TypeError("el argumento perfiles debe ser lista")
    ############################################################
    nuevo_usuario=input("Ingrese su nuevo usuario: ")

    while (func_aux.usuario_existente(perfiles,nuevo_usuario)):
        nuevo_usuario=input("Usuario existente ingrese otro: ")
        
    for perfil in perfiles:
        if perfil.get("usuario")==usuario:
            verificacion= input("Ingrese su clave: ")
            while not func_aux.verificar_clave(perfil.get("contrasenia"),verificacion):
                verificacion= input("Error clave incorrecta, vuelva a intentar: ")
            perfil["usuario"]=nuevo_usuario
            print("se pudo modificar")
            return 0
    """
    for llave in perfil.keys():
        if(llave_predeterminada==llave):
            perfil[llave]=nuevo_valor
            print("se modifico el perfil")
            return 0 
    """
    print("no se pudo modificar")
    return 1
#funcion modificar perfil terminado, devuelve un 0 si modifico el perfil 1 sino se pudo modificar 