"""Ejercicio 2: Sistema de gestión de equipos del Laboratorio Central de Investigación."""

CAPACIDAD_MAXIMA = 20
equipos_disponibles = CAPACIDAD_MAXIMA
historial_usos = 0

print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Equipos disponibles.")
    print("2.- Asignar equipo.")
    print("3.- Liberar equipo.")
    print("4.- Historial de usos.")
    print("5.- Salir.")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: debes ingresar un número del 1 al 5.")
        continue

    if opcion == 1:
        print(f"Equipos disponibles: {equipos_disponibles}")

    elif opcion == 2:
        # Cantidad a asignar (mayor a 0)
        while True:
            try:
                cantidad_asignar = int(input("Ingrese la cantidad de equipos a asignar: "))
                if cantidad_asignar > 0:
                    break
                print("Error: la cantidad debe ser mayor a 0.")
            except ValueError:
                print("Error: debes ingresar un número entero.")

        if cantidad_asignar > equipos_disponibles:
            print(f"No hay suficientes equipos disponibles. Solo quedan {equipos_disponibles}.")
        else:
            equipos_disponibles -= cantidad_asignar
            historial_usos += cantidad_asignar
            print(f"Se asignaron {cantidad_asignar} equipos correctamente.")

    elif opcion == 3:
        # Cantidad a liberar (mayor a 0)
        while True:
            try:
                cantidad_liberar = int(input("Ingrese la cantidad de equipos a liberar: "))
                if cantidad_liberar > 0:
                    break
                print("Error: la cantidad debe ser mayor a 0.")
            except ValueError:
                print("Error: debes ingresar un número entero.")

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