import requests
from sesion import TOKEN, URL_BASE
from datetime import datetime

def crear_dispositivo():
    print("\nCreando un nuevo dispositivo...")
    tipo_dispositivo = input("Ingrese el tipo de dispositivo (dron/robot): ")
    color = input("Ingrese el color del dispositivo: ")
    modelo = input("Ingrese el modelo del dispositivo: ")
    marca = input("Ingrese la marca del dispositivo: ")
    nivel_bateria = int(input("Ingrese el nivel de batería del dispositivo: "))
    estado = input("Ingrese el estado del dispositivo (activo/inactivo): ")

    url = URL_BASE + "create/"

    datos = {
        "tipo_dispositivo": tipo_dispositivo,
        "color": color,
        "modelo": modelo,
        "marca": marca,
        "nivel_bateria": nivel_bateria,
        "estado": estado
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.post(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nDispositivo creado con éxito.\n")
    else:
        print("\nError al crear el dispositivo. Por favor intente nuevamente.\n")

def obtener_dispositivo():
    dispositivo_id = input("Ingrese el ID del dispositivo que desea obtener: ")
    url = URL_BASE + f"read/{dispositivo_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nInformación del dispositivo obtenida con éxito:\n")
        print(respuesta.json())
    else:
        print("\nError al obtener la información del dispositivo. Por favor intente nuevamente.\n")

def actualizar_dispositivo():
    dispositivo_id = input("Ingrese el ID del dispositivo que desea actualizar: ")

    print("Ingrese la nueva información del dispositivo...")
    tipo_dispositivo = input("Ingrese el tipo de dispositivo (dron/robot): ")
    color = input("Ingrese el color del dispositivo: ")
    modelo = input("Ingrese el modelo del dispositivo: ")
    marca = input("Ingrese la marca del dispositivo: ")
    nivel_bateria = int(input("Ingrese el nivel de batería del dispositivo: "))
    estado = input("Ingrese el estado del dispositivo (activo/inactivo): ")

    url = URL_BASE + f"update/{dispositivo_id}/"

    datos = {
        "tipo_dispositivo": tipo_dispositivo,
        "color": color,
        "modelo": modelo,
        "marca": marca,
        "nivel_bateria": nivel_bateria,
        "estado": estado
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.put(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nDispositivo actualizado con éxito.\n")
    else:
        print("\nError al actualizar el dispositivo. Por favor intente nuevamente.\n")

def eliminar_dispositivo():
    dispositivo_id = input("Ingrese el ID del dispositivo que desea eliminar: ")
    url = URL_BASE + f"delete/{dispositivo_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.delete(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nDispositivo eliminado con éxito.\n")
    else:
        print("\nError al eliminar el dispositivo. Por favor intente nuevamente.\n")

def administrar_inventario():
    print("\nAdministrar inventario")
    print("1. Crear dispositivo")
    print("2. Obtener dispositivo")
    print("3. Actualizar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Regresar al menú principal")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        crear_dispositivo()
    elif opcion == "2":
        obtener_dispositivo()
    elif opcion == "3":
        actualizar_dispositivo()
    elif opcion == "4":
        eliminar_dispositivo()
    elif opcion == "5":
        return
    else:
        print("\nOpción no válida, intente nuevamente\n")
