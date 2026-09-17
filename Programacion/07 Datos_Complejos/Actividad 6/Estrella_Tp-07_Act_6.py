
#Actividad 6
alumnos = {}
promedio = {}
for alumno in range(3):
    nombre_valido = False
    while nombre_valido == False:
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre.title() not in alumnos and nombre.isalpha():
            nombre_valido = True
            break
        else:
            print("El nombre no es valido")
    notas = []

    for nota in range(3):
        while True:
            nota_ingresada = input("Ingrese la nota : ")
            if nota_ingresada.isnumeric():
                nota_ingresada = float(nota_ingresada)
            else:
                print("La nota ingresada no es válida. Por favor, ingrese una nota válida.")
            if 0 <= nota_ingresada <= 10:
                break
            else:
                print("La nota ingresada no está en el rango válido. Por favor, ingrese una nota del rango (0-10).")
        notas.append(nota_ingresada)
    promedio[nombre] = sum(notas) / len(notas)
    alumnos[nombre] = notas
    notas = tuple(notas)

for alumno in alumnos:
    print(f"El promedio del alumno {alumno} es: {promedio[alumno]:.2f} y las notas son: {alumnos[alumno]}")
    