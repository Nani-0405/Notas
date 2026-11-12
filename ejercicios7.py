"""Ejercicio 1: Registro de científicos del Instituto de Investigación Avanzada."""

total_principales = 0
total_asistentes = 0

# Cantidad de científicos a registrar (entero positivo)
while True:
    try:
        cantidad_cientificos = int(input("¿Cuántos científicos desea registrar? "))
        if cantidad_cientificos > 0:
            break
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
    except ValueError:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

for numero_cientifico in range(1, cantidad_cientificos + 1):
    print(f"\n--- Registro del científico {numero_cientifico} ---")

    # ID del científico (mínimo 6 caracteres y sin espacios)
    while True:
        id_cientifico = input("Ingrese el ID del científico: ")
        if len(id_cientifico) < 6:
            print("¡ID inválido! Debe tener al menos 6 caracteres.")
        elif " " in id_cientifico:
            print("¡ID inválido! No debe incluir espacios.")
        else:
            break

    # Número de publicaciones (entero positivo)
    while True:
        try:
            publicaciones = int(input("Ingrese el número de publicaciones: "))
            if publicaciones > 0:
                break
            print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
        except ValueError:
            print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")

    # Clasificación y contadores
    if publicaciones > 10:
        total_principales += 1
        print(f"El científico {id_cientifico} es un Investigador Principal.")
    else:
        total_asistentes += 1
        print(f"El científico {id_cientifico} es un Investigador Asistente.")

print(
    f"\n¡El instituto cuenta con {total_principales} Investigadores Principales "
    f"y {total_asistentes} Investigadores Asistentes! ¡Ciencia en marcha!"
)