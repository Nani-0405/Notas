"""Ejercicio 1: Registro de científicos del Instituto de Investigación Avanzada."""


def pedir_entero_positivo(mensaje, mensaje_error):
    """Pide un número entero positivo y repite hasta recibir uno válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print(mensaje_error)
        except ValueError:
            print(mensaje_error)


def pedir_id_cientifico():
    """Pide un ID de al menos 6 caracteres y sin espacios."""
    while True:
        id_cientifico = input("Ingrese el ID del científico: ")
        if len(id_cientifico) < 6:
            print("¡ID inválido! Debe tener al menos 6 caracteres.")
        elif " " in id_cientifico:
            print("¡ID inválido! No debe incluir espacios.")
        else:
            return id_cientifico


def main():
    total_principales = 0
    total_asistentes = 0

    cantidad_cientificos = pedir_entero_positivo(
        "¿Cuántos científicos desea registrar? ",
        "¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.",
    )

    for numero_cientifico in range(1, cantidad_cientificos + 1):
        print(f"\n--- Registro del científico {numero_cientifico} ---")

        id_cientifico = pedir_id_cientifico()

        publicaciones = pedir_entero_positivo(
            "Ingrese el número de publicaciones: ",
            "¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.",
        )
 
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


main()