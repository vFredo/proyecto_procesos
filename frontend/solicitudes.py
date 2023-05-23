import requests
import json
from sesion import TOKEN
from datetime import datetime

URL_BASE = "http://localhost:8001/api/v1/solicitudes/"

def crear_solicitud():
    print("\nCreando una nueva solicitud...\n")
    user_id = input("Ingrese el ID del usuario: ")
    
    # Solicita al usuario la fecha y hora en formato específico (YYYY-MM-DD HH:MM:SS)
    fecha_domicilio_input = input("Ingrese la fecha y hora del domicilio (formato AAAA-MM-DD HH:MM:SS): ")

    # Convierte la entrada del usuario a un objeto datetime
    fecha_domicilio_datetime = datetime.strptime(fecha_domicilio_input, "%Y-%m-%d %H:%M:%S")

    # Convierte el objeto datetime a formato ISO
    fecha_domicilio = fecha_domicilio_datetime.isoformat()

    hora_llegada_input = input("Ingrese la fecha y hora de llegada del dispositivo (formato AAAA-MM-DD HH:MM:SS): ")
    hora_llegada_datetime = datetime.strptime(hora_llegada_input, "%Y-%m-%d %H:%M:%S")
    hora_llegada = hora_llegada_datetime.isoformat()

    hora_salida_input = input("Ingrese la fecha y hora de salida del dispositivo (formato AAAA-MM-DD HH:MM:SS): ")
    hora_salida_datetime = datetime.strptime(hora_salida_input, "%Y-%m-%d %H:%M:%S")
    hora_salida = hora_salida_datetime.isoformat()
    
    dispositivo_asociado = input("Ingrese el ID del dispositivo asociado: ")
    peso_carga = float(input("Ingrese el peso en Kilogramos de la carga: "))
    lugar_entrega = input("Ingrese el lugar de entrega: ")
    estado_entrega = input("Ingrese el estado de la entrega (completado/por realizar/no entregado): ")

    url = URL_BASE + "create/"

    datos = {
        "user_id": user_id,
        "fecha_domicilio": fecha_domicilio,
        "hora_llegada": hora_llegada,
        "hora_salida": hora_salida,
        "dispositivo_asociado": dispositivo_asociado,
        "peso_carga": peso_carga,
        "lugar_entrega": lugar_entrega,
        "estado_entrega": estado_entrega
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.post(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200: 
            print("\nSolicitud creada con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al crear la solicitud. Por favor intente nuevamente.")

def obtener_solicitud():
    solicitud_id = input("\nIngrese el ID de la solicitud que desea obtener: ")
    url = URL_BASE + f"read/{solicitud_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200: 
            print("\nInformación de la solicitud obtenida con éxito:\n")

            # Usar json.dumps con los argumentos indent y sort_keys para formatear la salida
            json_formatted_str = json.dumps(respuesta.json()['message'], indent=2, sort_keys=True, ensure_ascii=False)
            
            print(json_formatted_str)
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al obtener la solicitud. Por favor intente nuevamente.")

def actualizar_solicitud():
    solicitud_id = input("\nIngrese el ID de la solicitud que desea actualizar: ")

    print("\nIngrese la nueva información de la solicitud...\n")
    user_id = input("Ingrese el ID del usuario: ")
    
    # Solicita al usuario la fecha y hora en formato específico (YYYY-MM-DD HH:MM:SS)
    fecha_domicilio_input = input("Ingrese la fecha y hora del domicilio (formato AAAA-MM-DD HH:MM:SS): ")

    # Convierte la entrada del usuario a un objeto datetime
    fecha_domicilio_datetime = datetime.strptime(fecha_domicilio_input, "%Y-%m-%d %H:%M:%S")

    # Convierte el objeto datetime a formato ISO
    fecha_domicilio = fecha_domicilio_datetime.isoformat()

    hora_llegada_input = input("Ingrese la fecha y hora de llegada del dispositivo (formato AAAA-MM-DD HH:MM:SS): ")
    hora_llegada_datetime = datetime.strptime(hora_llegada_input, "%Y-%m-%d %H:%M:%S")
    hora_llegada = hora_llegada_datetime.isoformat()

    hora_salida_input = input("Ingrese la fecha y hora de salida del dispositivo (formato AAAA-MM-DD HH:MM:SS): ")
    hora_salida_datetime = datetime.strptime(hora_salida_input, "%Y-%m-%d %H:%M:%S")
    hora_salida = hora_salida_datetime.isoformat()

    dispositivo_asociado = input("Ingrese el ID del dispositivo asociado: ")
    peso_carga = float(input("Ingrese el peso en Kilogramos de la carga: "))
    lugar_entrega = input("Ingrese el lugar de entrega: ")
    estado_entrega = input("Ingrese el estado de la entrega (completado/por realizar/no entregado): ")

    url = URL_BASE + f"update/{solicitud_id}/"

    datos = {
        "user_id": user_id,
        "fecha_domicilio": fecha_domicilio,
        "hora_llegada": hora_llegada,
        "hora_salida": hora_salida,
        "dispositivo_asociado": dispositivo_asociado,
        "peso_carga": peso_carga,
        "lugar_entrega": lugar_entrega,
        "estado_entrega": estado_entrega
    }

    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.put(url, json=datos, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200: 
            print("\nSolicitud actualizada con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al actualizar la solicitud. Por favor intente nuevamente.")

def eliminar_solicitud():
    solicitud_id = input("\nIngrese el ID de la solicitud que desea eliminar: ")
    url = URL_BASE + f"delete/{solicitud_id}/"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    respuesta = requests.delete(url, headers=headers)

    if respuesta.status_code == 200:
        if respuesta.json()['code'] == 200: 
            print("\nSolicitud eliminada con éxito.")
        else:
            print("\n" + respuesta.json()['message'])
    else:
        print("\nError al eliminar la solicitud. Por favor intente nuevamente.")

def administrar_solicitudes():
    print("\nAdministrar solicitudes\n")
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
        print("\nOpción no válida, intente nuevamente")
