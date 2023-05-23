import requests
import getpass

TOKEN = None
URL_BASE = "http://localhost:8000/api/v1/usuarios/"

def iniciar_sesion():
    global TOKEN

    usuario = input("\nIngrese el nombre de usuario: ")
    password = getpass.getpass("Ingrese la contraseña: ")

    url = URL_BASE + "login/"

    datos = {
        "user": usuario,
        "password": password
    }

    respuesta = requests.post(url, json=datos)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200: 
            TOKEN = respuesta.json()['message']['token']
            print("\nInicio de sesión exitoso.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError en el inicio de sesión. Por favor intente nuevamente.")
