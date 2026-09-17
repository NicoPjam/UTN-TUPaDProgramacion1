parcial_1 = set()
parcial_2 = set()

NOTA_APROBACION = 6

while True:
    legajo = input("\nIngrese el legajo/nombre del alumno: ").strip()

    while True:
        nota1 = float(input("Ingrese la nota del parcial 1: "))
        if 0 <= nota1 <= 10:
            break
        print("La nota ingresada no es válida (debe ser entre 0 y 10).")

    while True:
        nota2 = float(input("Ingrese la nota del parcial 2: "))
        if 0 <= nota2 <= 10:
            break
        print("La nota ingresada no es válida (debe ser entre 0 y 10).")

    if nota1 >= NOTA_APROBACION:
        parcial_1.add(legajo)

    if nota2 >= NOTA_APROBACION:
        parcial_2.add(legajo)

    opcion = input("¿Desea ingresar las notas de otro alumno? (S/N): ").strip().upper()
    if opcion == "N":
        break

aprob_ambos = parcial_1 & parcial_2
aprob_uno = parcial_1 ^ parcial_2
aprob_al_menos_uno = parcial_1 | parcial_2

print("\nResultados:")
print(f"\nAlumnos aprobados en ambos parciales: {aprob_ambos}")
print(f"Alumnos aprobados en un solo parcial: {aprob_uno}")
print(f"Alumnos aprobados en al menos un parcial: {aprob_al_menos_uno}")