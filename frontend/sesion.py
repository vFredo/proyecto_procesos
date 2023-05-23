import requests
import getpass

TOKEN = None
URL_BASE = "http://ejemplo.com/" # Puedes reemplazar esto por la URL de tu servidor

def iniciar_sesion():
    global TOKEN

    usuario = input("Ingrese el nombre de usuario: ")
    password = getpass.getpass("Ingrese la contraseña: ")

    url = URL_BASE + "login/"

    datos = {
        "user": usuario,
        "password": password
    }

    #respuesta = requests.post(url, json=datos)
    respuesta = {
        "message": {
            "token": ""
        }
    }

    #if respuesta.status_code == 200:
    if True:
        #TOKEN = respuesta.json()['message']['token']
        TOKEN = respuesta['message']['token']
        print("\nInicio de sesión exitoso.\n")
    else:
        print("\nError en el inicio de sesión. Por favor intente nuevamente.\n")
