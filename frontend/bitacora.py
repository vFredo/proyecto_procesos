import requests
import json
from sesion import TOKEN
from datetime import datetime

URL_BASE = "http://localhost:8004/api/v1/bitacora/"

def crear_anotacion():
    print("\nCreando una nueva anotacion...\n")
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
        if respuesta.json()['code'] == 200: 
            print("\nAnotación creada con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al crear la anotación. Por favor intente nuevamente.")

def obtener_anotacion_dispositivo():
    dispositivo_id = input("\nIngrese el ID del dispositivo para obtener sus anotaciones: ")
    url = URL_BASE + f"dispositivo/{dispositivo_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200:
            print("\nInformación de las anotaciones obtenida con éxito:\n")

            anotaciones = respuesta.json()['message']
            
            for anotacion in anotaciones:
                # Usar json.dumps con los argumentos indent y sort_keys para formatear la salida
                json_formatted_str = json.dumps(anotacion, indent=2, sort_keys=True, ensure_ascii=False)
                
                print(json_formatted_str)
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al obtener las anotaciones del dispositivo. Por favor intente nuevamente.")

def actualizar_anotacion():
    anotacion_id = input("\nIngrese el ID de la anotación que desea actualizar: ")

    print("\nIngrese la nueva información de la anotación...\n")
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
        if respuesta.json()['code'] == 200:
            print("\nAnotación actualizada con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al actualizar la anotación. Por favor intente nuevamente.")

def eliminar_anotacion():
    anotacion_id = input("\nIngrese el ID de la anotación que desea eliminar: ")
    url = URL_BASE + f"delete/{anotacion_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.delete(url, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200:
            print("\nAnotación eliminada con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al eliminar la anotación. Por favor intente nuevamente.")

def administrar_bitacora():
    print("\nAdministrar bitacora\n")
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
        print("\nOpción no válida, intente nuevamente")
