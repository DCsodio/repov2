import func_aux 
"""
-mostrar_perfiles
-modificar_perfil
-crear_perfil
-loguear
-menu inicio
"""
def mostrar_perfiles(perfiles:list):
    if not isinstance(perfiles,list):
        raise TypeError("El argumento 'perfiles' debe ser lista")
    for perfil in perfiles:
        if not isinstance(perfil,dict):
            raise TypeError("el contenido de'perfiles' deben ser dict")
        
    for perfil in range (len(perfiles)):
        print(f"perfil: {perfil}")
        for usuario,clave in perfiles[perfil].items():
            print(f"{usuario}={clave}")
    if len(perfiles)==0:
        print("No hay usuarios")

#funcion mostrar perfil terminado, Muestra perfiles
 


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
    
    perfiles.append({"usuario":usuario_ing,"contrasenia":clave_ing})
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
    print("3- Login")

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
        clave_hasheado= perfiles[perfil].get("contrasenia")
        if (func_aux.verificar_clave(clave_hasheado,clave_ingr)):
            return True
        
    print("error ID")
    return False
#listo funcion, devuleve 0 si se pudo loguear 1 sino pudo