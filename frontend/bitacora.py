import requests
from sesion import TOKEN, URL_BASE
from datetime import datetime

def crear_anotacion():
    print("\nCreando una nueva anotacion...")
    id_dispositivo = input("Ingrese el ID del dispositivo: ")
    fecha = datetime.now()
    anotacion = input("Ingrese la anotación: ")

    url = URL_BASE + "create/"

    datos = {
        "id_dispositivo": id_dispositivo,
        "fecha": fecha.isoformat(),
        "anotacion": anotacion
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.post(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nAnotación creada con éxito.\n")
    else:
        print("\nError al crear la anotación. Por favor intente nuevamente.\n")

def obtener_anotacion_dispositivo():
    dispositivo_id = input("Ingrese el ID del dispositivo para obtener sus anotaciones: ")
    url = URL_BASE + f"dispositivo/{dispositivo_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nInformación de las anotaciones obtenida con éxito:\n")
        print(respuesta.json())
    else:
        print("\nError al obtener las anotaciones del dispositivo. Por favor intente nuevamente.\n")

def actualizar_anotacion():
    anotacion_id = input("Ingrese el ID de la anotación que desea actualizar: ")

    print("Ingrese la nueva información de la anotación...")
    id_dispositivo = input("Ingrese el ID del dispositivo: ")
    anotacion = input("Ingrese la anotación: ")

    url = URL_BASE + f"update/{anotacion_id}/"

    datos = {
        "id_dispositivo": id_dispositivo,
        "fecha": datetime.now().isoformat(),
        "anotacion": anotacion
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.put(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nAnotación actualizada con éxito.\n")
    else:
        print("\nError al actualizar la anotación. Por favor intente nuevamente.\n")

def eliminar_anotacion():
    anotacion_id = input("Ingrese el ID de la anotación que desea eliminar: ")
    url = URL_BASE + f"delete/{anotacion_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.delete(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nAnotación eliminada con éxito.\n")
    else:
        print("\nError al eliminar la anotación. Por favor intente nuevamente.\n")

def administrar_bitacora():
    print("\nAdministrar bitacora")
    print("1. Crear anotación")
    print("2. Obtener anotaciones dispositivo")
    print("3. Actualizar anotación")
    print("4. Eliminar anotación")
    print("5. Regresar al menú principal")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        crear_anotacion()
    elif opcion == "2":
        obtener_anotacion_dispositivo()
    elif opcion == "3":
        actualizar_anotacion()
    elif opcion == "4":
        eliminar_anotacion()
    elif opcion == "5":
        return
    else:
        print("\nOpción no válida, intente nuevamente\n")
