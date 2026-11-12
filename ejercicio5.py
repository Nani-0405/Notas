"""Ejercicio 2: Sistema de gestión de equipos del Laboratorio Central de Investigación."""

CAPACIDAD_MAXIMA = 20


def pedir_cantidad(mensaje):
    """Pide una cantidad entera mayor a 0 y repite hasta recibir una válida."""
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad > 0:
                return cantidad
            print("Error: la cantidad debe ser mayor a 0.")
        except ValueError:
            print("Error: debes ingresar un número entero.")

 
def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Equipos disponibles.")
    print("2.- Asignar equipo.")
    print("3.- Liberar equipo.")
    print("4.- Historial de usos.")
    print("5.- Salir.")


def main():
    equipos_disponibles = CAPACIDAD_MAXIMA
    historial_usos = 0

    print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debes ingresar un número del 1 al 5.")
            continue

        if opcion == 1:
            print(f"Equipos disponibles: {equipos_disponibles}")

        elif opcion == 2:
            cantidad_asignar = pedir_cantidad("Ingrese la cantidad de equipos a asignar: ")
            if cantidad_asignar > equipos_disponibles:
                print(
                    f"No hay suficientes equipos disponibles. "
                    f"Solo quedan {equipos_disponibles}."
                )
            else:
                equipos_disponibles -= cantidad_asignar
                historial_usos += cantidad_asignar
                print(f"Se asignaron {cantidad_asignar} equipos correctamente.")

        elif opcion == 3:
            cantidad_liberar = pedir_cantidad("Ingrese la cantidad de equipos a liberar: ")
            if equipos_disponibles + cantidad_liberar > CAPACIDAD_MAXIMA:
                print(
                    f"No se puede liberar esa cantidad: superaría la capacidad "
                    f"máxima del laboratorio ({CAPACIDAD_MAXIMA} equipos)."
                )
            else:
                equipos_disponibles += cantidad_liberar
                historial_usos -= cantidad_liberar
                print(f"Se liberaron {cantidad_liberar} equipos correctamente.")

        elif opcion == 4:
            print(f"Total de equipos asignados durante la sesión: {historial_usos}")

        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break

        else:
            print("Opción inválida. Elige un número del 1 al 5.")


main()