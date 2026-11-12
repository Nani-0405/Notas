print("==== BIENVENIDO AL SISTEMA DE REGISTROS DE CIENTIFICOS =======\n")

while True:
    cientificos = int(input("Ingrese la cantidad de cientificos a registrar: "))

    if cientificos <= 0:
        print("Dato de investigación inválido! Ingresa un entero positivo para continuar con el registro.....")
    else:
        print("Registro exitoso!")
        break

investigador_Asistente = 0
investigador_Principal = 0

for i in range(1, cientificos + 1):
    print(f"\n ===== Registrando cientifico {i} de {cientificos} =====")

    while True:
        id_Cientifico = input("Ingrese un ID minimo de 12 caracteres: ").strip()
        if len(id_Cientifico) >= 12:
            print("Ingresaste un id válido.....")
            break
        else:
            print("Error, el id debe de contener a lo menos 12 caracteres, intentelo nuevamente.....")

    while True:
        num_Publicaciones = int(input("Numero de publicaciones del cientifico: "))
        if num_Publicaciones >= 1:
            break
        else:
            print("Error de registro! Ingresa un numero entero positivo para el numero de publicaciones")

    if num_Publicaciones >= 12:
        investigador_Principal += 1
        print("Clasificado como investigador principal.")
    else:
        investigador_Asistente += 1
        print("Clasificado como investigador asistente.")

print("\n" + "=" * 65)
print(f"Investigadores principales: {investigador_Principal}")
print(f"Investigadores asistentes: {investigador_Asistente}")
print("=" * 65)