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


def crear_perfil(perfiles:list, usuario_ing:str, clave_ing:str):
     
    if not (isinstance(usuario_ing, dict) or isinstance(perfiles, list) or isinstance(clave_ing,str)):
        raise TypeError("revise los argumentos")
    for perfil in perfiles:
        if not isinstance(perfil, dict):
            raise TypeError("revise el argumento de la lista diccionario")
    #listo prote

    #aca me va a llegar un perfil no repetido ya listo para procesar
    
    perfiles.append({"usuario":usuario_ing,"clave":clave_ing})
    if usuario_ing==perfiles[len(perfiles)-1].get("usuario"):
        print(f"se agrego el usuario: {perfiles[len(perfiles)-1].get("usuario")} correctamente")
        return 0
    else:
        print(f"Crear usuario fallo")
        return 1
#funcion crear perfil terminada, agrega un perfil a la lista de diccionarios (perfiles), devuelve 0 si puedo sino 1

def login(perfiles:list, usuario_ingr:str, contrasenia_ingr:str):
    if not (isinstance(perfiles,dict) or isinstance(usuario_ingr,dict) or isinstance(contrasenia_ingr,str)):
        raise TypeError("argumentos invalidos")
    for perfil in perfiles:
        if not isinstance(perfil, dict):
            raise TypeError("perfiles no contiene diccionarios")
    #listo protecciones

    for perfil in range(len(perfiles)):
        usuario= perfiles[perfil].get("usuario")
        clave= perfiles[perfil].get("contrasenia")
        #print(f"{usuario}:{clave}")
        if (usuario_ingr==usuario and contrasenia_ingr==clave):
            print("te logueaste")
            return 0
    print("error ID")
    return 1
#listo funcion, devuleve 0 si se pudo loguear 1 sino pudo