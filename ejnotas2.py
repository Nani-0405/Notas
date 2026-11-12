equipos_disponibles = 25
total_equipos_liberado = 0
total_equipos_asignado = 0

while True:
    try:
        print("""
======== ¡BIENVENIDOS AL SISTEMA DE GESTION DE EQUIPOS DEL LABORATORIO CENTRAL DE INVESTIGACION! ========
1.- Equipos disponibles
2.- Asignar equipos
3.- Liberar equipos
4.- Historial de uso
5.- Salir
======================================================================================================""")
        opcion = int(input("\nIngrese una opción: "))
    except ValueError:
        print("Error, ingrese un valor entero válido.")
        continue

    match opcion:
        case 1:
            print("La cantidad de equipos disponibles es de", equipos_disponibles)

        case 2:
            try:
                equipos_asignar = int(input("Equipos a asignar: "))
                if equipos_asignar <= 0:
                    print("Error, debe ser mayor a 0.")
                elif equipos_asignar > equipos_disponibles:
                    print("No puede superar los equipos disponibles, que son:", equipos_disponibles)
                else:
                    equipos_disponibles -= equipos_asignar
                    total_equipos_asignado += equipos_asignar
                    print(f"Se asignaron {equipos_asignar} equipos. Equipos disponibles: {equipos_disponibles}")
            except ValueError:
                print("Error, ingrese un número válido.")

        case 3:
            try:
                liberar_equipos = int(input("Equipos a liberar: "))
                equipos_en_uso = 25 - equipos_disponibles
                if liberar_equipos <= 0:
                    print("Error, debe ser mayor a 0.")
                elif liberar_equipos > equipos_en_uso:
                    print(f"Error, no puede superar los equipos en uso, que son: {equipos_en_uso}")
                else:
                    equipos_disponibles += liberar_equipos
                    total_equipos_liberado += liberar_equipos
                    print(f"Se liberaron {liberar_equipos} equipos. Equipos disponibles: {equipos_disponibles}")
            except ValueError:
                print("Error, ingrese un número válido.")

        case 4:
            print("=========== HISTORIAL DE USO ==========")
            print(f"Total de equipos asignados: {total_equipos_asignado}")
            print(f"Total de equipos liberados: {total_equipos_liberado}")
            print(f"Equipos disponibles: {equipos_disponibles}")
            print("=======================================")

        case 5:
            try:
                respuesta = int(input("\nDesea salir (0.- Si 1.- No): "))
                if respuesta == 0:
                    print("Gracias por usar nuestro software, hasta la próxima!")
                    break
                elif respuesta == 1:
                    print("Continuemos con los registros....")
                else:
                    print("Opción inválida, ingrese 0 o 1.")
            except ValueError:
                print("Error, ingresa un número válido.")

        case _:
            print("Opción inválida, las opciones van del 1 al 5.")