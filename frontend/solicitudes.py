import requests
from sesion import TOKEN, URL_BASE
from datetime import datetime

def crear_solicitud():
    print("\nCreando una nueva solicitud...")
    user_id = input("Ingrese el ID del usuario: ")
    fecha_domicilio = datetime.now().isoformat()
    hora_llegada = datetime.now().isoformat()
    hora_salida = datetime.now().isoformat()
    solicitud_asociado = input("Ingrese el solicitud asociado: ")
    peso_carga = float(input("Ingrese el peso de la carga: "))
    lugar_entrega = input("Ingrese el lugar de entrega: ")
    estado_entrega = input("Ingrese el estado de la entrega (completado/por realizar/no entregado): ")

    url = URL_BASE + "create/"

    datos = {
        "user_id": user_id,
        "fecha_domicilio": fecha_domicilio,
        "hora_llegada": hora_llegada,
        "hora_salida": hora_salida,
        "solicitud_asociado": solicitud_asociado,
        "peso_carga": peso_carga,
        "lugar_entrega": lugar_entrega,
        "estado_entrega": estado_entrega
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.post(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nSolicitud creada con éxito.\n")
    else:
        print("\nError al crear la solicitud. Por favor intente nuevamente.\n")

def obtener_solicitud():
    solicitud_id = input("Ingrese el ID de la solicitud que desea obtener: ")
    url = URL_BASE + f"read/{solicitud_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nInformación de la solicitud obtenida con éxito:\n")
        print(respuesta.json())
    else:
        print("\nError al obtener la solicitud. Por favor intente nuevamente.\n")

def actualizar_solicitud():
    solicitud_id = input("Ingrese el ID de la solicitud que desea actualizar: ")

    print("Ingrese la nueva información de la solicitud...")
    user_id = input("Ingrese el ID del usuario: ")
    fecha_domicilio = datetime.now().isoformat()
    hora_llegada = datetime.now().isoformat()
    hora_salida = datetime.now().isoformat()
    solicitud_asociado = input("Ingrese el solicitud asociado: ")
    peso_carga = float(input("Ingrese el peso de la carga: "))
    lugar_entrega = input("Ingrese el lugar de entrega: ")
    estado_entrega = input("Ingrese el estado de la entrega (completado/por realizar/no entregado): ")

    url = URL_BASE + f"update/{solicitud_id}/"

    datos = {
        "user_id": user_id,
        "fecha_domicilio": fecha_domicilio,
        "hora_llegada": hora_llegada,
        "hora_salida": hora_salida,
        "solicitud_asociado": solicitud_asociado,
        "peso_carga": peso_carga,
        "lugar_entrega": lugar_entrega,
        "estado_entrega": estado_entrega
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.put(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        print("\nSolicitud actualizada con éxito.\n")
    else:
        print("\nError al actualizar la solicitud. Por favor intente nuevamente.\n")

def eliminar_solicitud():
    solicitud_id = input("Ingrese el ID de la solicitud que desea eliminar: ")
    url = URL_BASE + f"delete/{solicitud_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.delete(url, headers=headers)

    if respuesta.status_code == 200:
        print("\nSolicitud eliminada con éxito.\n")
    else:
        print("\nError al eliminar la solicitud. Por favor intente nuevamente.\n")

def administrar_solicitudes():
    print("\nAdministrar solicitudes")
    print("1. Crear solicitud")
    print("2. Obtener solicitud")
    print("3. Actualizar solicitud")
    print("4. Eliminar solicitud")
    print("5. Regresar al menú principal")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        crear_solicitud()
    elif opcion == "2":
        obtener_solicitud()
    elif opcion == "3":
        actualizar_solicitud()
    elif opcion == "4":
        eliminar_solicitud()
    elif opcion == "5":
        return
    else:
        print("\nOpción no válida, intente nuevamente\n")
