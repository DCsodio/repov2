"""
-usuario_existente
-ingreso_id
"""


def usuario_existente(perfiles, usuario:str):
    if not isinstance(usuario,str):
        raise TypeError("usuario debe ser str")
    if not isinstance(perfiles,list):
        raise TypeError("perfiles debe ser list")
    
    for perfil in perfiles:
        if not isinstance(perfil, dict):
            raise TypeError("perfiles debe contener diccionarios")
    #listo protecciones

    for perfil in  perfiles:
        if(usuario==perfil.get("usuario")):
            return True   
    return False
#LISTO DETECTOR DE USUARIO EXISTENTE, DEVUELVE TRUE SI DETECTO SINO FALSE

def ingreso_id(usuario,clave):
    print("Bienvenido a la nueva version del servidor de musica 2.0")
    print("///////////////////////////////////")
    usuario=input("Ingrese su usuario: ")
    clave=inpu

#probador
if __name__== "__main__":
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

    usuario_existente(perfiles, "caro12354")