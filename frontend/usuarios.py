import requests
import getpass
from sesion import TOKEN, URL_BASE

def crear_usuario():
    usuario = input("\nIngrese el nombre de usuario: ")
    password = getpass.getpass("Ingrese la contraseña: ")

    url = URL_BASE + "post/"

    datos = {
        "user": usuario,
        "password": password,
        "multas": 0,
        "deuda": 0.0
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.post(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200: 
            print("\nUsuario creado con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al crear el usuario. Por favor intente nuevamente.")

def eliminar_usuario():
    usuario_id = input("\nIngrese el ID del usuario a eliminar: ")

    url = URL_BASE + "delete/" + usuario_id

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.delete(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nUsuario eliminado con éxito.")
    else:
        print("\nError al eliminar el usuario. Por favor intente nuevamente.")

def actualizar_password():
    usuario_id = input("\nIngrese el ID del usuario a actualizar: ")
    password = getpass.getpass("Ingrese la nueva contraseña: ")

    url = URL_BASE + "password/" + usuario_id

    datos = {
        "password": password
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.put(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nContraseña actualizada con éxito.")
    else:
        print("\nError al actualizar la contraseña. Por favor intente nuevamente.")

def administrar_usuarios():
    print("\nAdministrar usuarios\n")
    print("1. Crear usuario")
    print("2. Eliminar usuario")
    print("3. Actualizar contraseña")
    print("4. Regresar al menú principal")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        eliminar_usuario()
    elif opcion == "3":
        actualizar_password()
    elif opcion == "4":
        return
    else:
        print("\nOpción no válida, intente nuevamente")