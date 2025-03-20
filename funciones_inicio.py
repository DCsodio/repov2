import func_aux 
"""
-mostrar_perfiles
-modificar_perfil
-crear_perfil
-loguear
"""
def mostrar_perfiles(perfiles:list):
    if not isinstance(perfiles,list):
        raise TypeError("El argumento 'perfiles' debe ser lista")
    
    for perfil in perfiles:
        if not isinstance(perfil,dict):
            raise TypeError("el contenido de'perfiles' deben ser dict")

    for perfil in range (len(perfiles)):
        print(f"perfil: {perfil}")
        for parametro,datos in perfiles[perfil].items():
            print(f"{parametro}={datos}")

#funcion mostrar perfil terminado, Muestra perfiles

def modificar_perfil(llave_predeterminada:str, nuevo_valor:str, perfil:dict):
    if not isinstance(perfil, dict):    #proteccion
        raise TypeError("el argumento 'perfil' debe ser un diccionario")
    """
        raise TypeError ("falla")  detiene el programa
        isistance (variable, formato) #si coincide manda true 
    """
    if not isinstance(llave_predeterminada,str) or not isinstance(nuevo_valor,str): #proteccion
        raise TypeError("el argumento 'llave_predeterminada' y 'nuevo_valor' debe ser str")

    for llave in perfil.keys():
        if(llave_predeterminada==llave):
            perfil[llave]=nuevo_valor
            print("se modifico el perfil")
            return 0 
    
    print("no se pudo modificar")
    return 1
#funcion modificar perfil terminado, devuelve un 0 si modifico el perfil 1 sino se pudo modificar  


def crear_perfil(perfiles:list):
     
    if not isinstance(perfiles, list):
        raise TypeError("revise los argumentos")
    for perfil in perfiles:
        if not isinstance(perfil, dict):
            raise TypeError("revise el argumento de la lista diccionario")
    #listo prote

    #aca me va a llegar un perfil no repetido ya listo para procesar
    usuario_ing=input("Ingrese su nuevo usuario: ")
    se_repite=func_aux.usuario_existente(perfiles,usuario_ing)
    while(se_repite==True):
        print("¡Usuario repetido!")
        suario_ing=input("Vuelva a ingresear un usuario disponibles: ")
        se_repite=func_aux.usuario_existente(perfiles,usuario_ing)

    clave_ing=input("Ingrese su contraseña: ")
    verificacion=input("Ingrese nuevamente su contraseña: ")

    while clave_ing!=verificacion:
        print("-Contraseñas no coinciden-")
        clave_ing=input("Ingrese su contraseña: ")
        verificacion=input("Ingrese nuevamente su contraseña: ")        

    clave_ing= func_aux.encriptar_clave(clave_ing)
    
    perfiles.append({"usuario":usuario_ing,"clave":clave_ing})
    if usuario_ing==perfiles[len(perfiles)-1].get("usuario"):
        print(f"se agrego el usuario: {perfiles[len(perfiles)-1].get("usuario")} correctamente")
        return 0
    else:
        print(f"Crear usuario fallo")
        return 1
#funcion crear perfil terminada, agrega un perfil a la lista de diccionarios (perfiles), devuelve 0 si puedo sino 1

def cambiar_clave (clave_encriptada:bytes, usuario:str ,perfiles:list):

    if not(isinstance (clave_encriptada,bytes) or isinstance(perfiles,list) or isinstance(usuario,str)):
        raise TypeError("Error en argumentos clave_encriptada o perfiles")
    for perfil in perfiles:
        if not isinstance(perfil,dict):
            raise TypeError("Error en argumento perfiles")

    print("Seccion cambiar contraseña")

    nueva_clave=input("ingrese nueva clave: ")
    verificacion=input("ingrese nuevamente su nueva clave: ")

    while nueva_clave!=verificacion:
        verificacion=input("error claves distintas\n ingrese nuevamente su nueva clave: ")

    clave_anterior=input("confirme su clave actual: ")

    if func_aux.verificar_clave(clave_encriptada,clave_anterior):
        for perfil in perfiles:
            if usuario==perfil.get("usuario"):
                perfil["contrasenia"]=func_aux.encriptar_clave(nueva_clave.encode())



def menu_inicio():
    
    print("Bienvenido a la nueva version del servidor de musica 2.0")
    print("///////////////////////////////////")
    print("0- Salir")
    print("1- Crear perfil")
    print("2- Mostrar perfiles")

    opcion=int(input("ingrese una de las opciones: "))

    return opcion

        


def login(perfiles:list, usuario_ingr:str, clave_ingr:str):
    if not (isinstance(perfiles,dict) or isinstance(usuario_ingr,dict) or isinstance(clave_ingr,str)):
        raise TypeError("argumentos invalidos")
    for perfil in perfiles:
        if not isinstance(perfil, dict):
            raise TypeError("perfiles no contiene diccionarios")
    #listo protecciones

    for perfil in range(len(perfiles)):
        usuario= perfiles[perfil].get("usuario")
        clave= perfiles[perfil].get("contrasenia")
        #print(f"{usuario}:{clave}")
        if (usuario_ingr==usuario and clave_ingr==clave):
            print("te logueaste")
            return 0
    print("error ID")
    return 1
#listo funcion, devuleve 0 si se pudo loguear 1 sino pudo