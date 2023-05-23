import sesion
import inventario
import bitacora
import usuarios
import solicitudes
import domicilio
import utils

def main():
    while True:
        utils.clear_console()
        print("Seleccione una opción:\n")
        print("1. Iniciar sesión") if sesion.TOKEN is None else None
        print("2. Salir") if sesion.TOKEN is None else None
        if sesion.TOKEN is not None:
            print("1. Administrar inventario")
            print("2. Administrar bitácora")
            print("3. Administrar usuarios")
            print("4. Administrar solicitudes")
            print("5. Simular domicilio")
            print("6. Salir")
        opcion = input("\nOpción: ")

        if opcion == "1" and sesion.TOKEN is None:
            sesion.iniciar_sesion()
        elif opcion == "2" and sesion.TOKEN is None:
            break
        elif opcion == "1" and sesion.TOKEN is not None:
            inventario.administrar_inventario()
        elif opcion == "2" and sesion.TOKEN is not None:
            bitacora.administrar_bitacora()
        elif opcion == "3" and sesion.TOKEN is not None:
            usuarios.administrar_usuarios()
        elif opcion == "4" and sesion.TOKEN is not None:
            solicitudes.administrar_solicitudes()
        elif opcion == "5" and sesion.TOKEN is not None:
            log_file = input("\nIngrese el nombre del archivo de log: ")
            domicilio.simular_domicilio(log_file)
        elif opcion == "6":
            break
        else:
            print("\nOpción no válida, intente nuevamente")

        input("\nPresione enter para continuar...")

if __name__ == "__main__":
    main()

