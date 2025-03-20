"""
-usuario_existente
-ingreso_id
-encriptar_clave
-verificar_clave
"""
import bcrypt

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

def ingreso_id():
    usuario=input("Ingrese su usuario: ")
    clave=input("Ingrese su contraseña: ")

    return usuario,clave

#LISTO INGRESO:ID, DEVUELVE USUARIO Y CLAVE.


#vamos a hashear la contraseña, usando bcrypt
#sudo apt install python3-pip
#sudo apt install python3.12-venv installamos venv para crear un entorno virtual
#en la carpeta del proyecto: python3 -m venv nombre_del_entorno
#source repov2/bin/activate
#pip install bcryp
#para deactivarlo deactive
#CONFIGURAR VSC PARA TOMAR EL INTERPRETE DEL ENTORNO


def encriptar_clave (clave:str):

    if not isinstance(clave,str):
        raise TypeError("ingrese var tipo byte")
    clave=clave.encode()
    salt=bcrypt.gensalt()
    clave_encriptada=bcrypt.hashpw(clave,salt)

    return clave_encriptada

def verificar_clave(clave_encriptada:bytes, clave:str):
    
    if not isinstance(clave,str):
        raise TypeError("ingrese var tipo str")
    else:
        clave=clave.encode() #lo paso a bytes

    return bcrypt.checkpw(clave,clave_encriptada) 
#VERIFICAR_PASS TERMINADO, DEVUELVE TRUE SI VERIFICA, SINO FALSE 









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
    print(bcrypt.__version__)