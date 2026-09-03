#Actividad N1

filas = int(input("Ingrese la cantidad de filas de la matriz! : "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz! : "))

matriz = []
numeros = 1
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(numeros)
        numeros += 1
print(f"la matriz es: {matriz} \n")

#Actividad N2

matriz = [
    [5, 10, 7],
    [8, 12, 3],
    [4, 2, 41]
] 
suma = sum(sum(fila) for fila in matriz)
print(f"la suma de todos los elementos de la matriz es: {suma} \n")

#Actividad N3

matriz = [
    [5, 10, 7],
    [8, 12, 3],
    [4, 2, 41]
] 
for fila in matriz:
    suma = sum(fila)
    print(f"la suma de la fila {fila} es: {suma} \n")

#Actividad N4

matriz_original = [
    [5, 10, 7],
    [8, 12, 3],
]
transpuesta = [[matriz.original[j][i] for j in range(len(matriz_original))] for i in range(len(matriz_original[0]))]   
print (f"la matriz transpuesta es:\n")
for fila in transpuesta:
    print(f"{fila}\n")

#Actividad N5

matriz = [
    [5, 10, 7],
    [8, 12, 3],
    [4, 2, 41]
]
matriz = [num for fila in matriz for num in fila]
Max_num = 0
for fila in matriz:
    for elemento in fila:
        if elemento > Max_num:
            Max_num = elemento
max_matriz = Max_num
print(f"el numero con maximo valor de la matriz es: {max_matriz} \n")


#Actividad N6

matriz = [
    [5, 10, 7],
    [8, 12, 3],
    [4, 2, 41]
]
multiplicador = int(input("Ingrese el multiplicador! : \n"))
matriz_resultante = [[elemento * multiplicador for elemento in fila] for fila in matriz]

print(f"\nla matriz original es\n")
for fila in matriz:
    print(f"{fila}\n")
print(f"\nla matriz resultante es:\n")
for fila in matriz_resultante:
    print(f"{fila}\n")

#Actividad N7

matriz = [
    [5, 10, 7],
    [8, 12, 3],
    [4, 2, 41]
]
diagonal = [matriz[valor][valor] for valor in range(len(matriz))]
print(f"La diagonal de la matriz es! : \n {diagonal} \n")

#Actividad N8

Rango = int(input("Ingrese el valor para el tamaño de la matriz identidad! en entero : \n"))
Matriz_identidad = [[1 if fila == columna else 0 for columna in range(Rango)] for fila in range(Rango)]

for fila in Matriz_identidad:
    print(f"{fila}\n")

#Actividad N9

Rango = int(input("Ingrese el valor para el tamaño de la matriz identidad! en entero : \n"))
Matriz_identidad = [[1 if fila == columna else 0 for columna in range(Rango)] for fila in range(Rango)]

print(f"la matriz identidad es:\n")
for fila in Matriz_identidad:
    print(f"{fila}\n")

#Actividad N10

Rango = int(input("Ingrese el valor N para el tamaño de la matriz identidad Inversa! en entero : \n"))
Matriz_identidad = [[1 if fila + columna == Rango - 1 else 0 for columna in range(Rango)] for fila in range(Rango)]

print(f"la matriz identidad inversa es:\n")
for fila in Matriz_identidad:
    print(f"{fila}\n")

#Actividad N11

matriz = [
    [5, 10, 7],
    [8, 12, 3],
    [4, 2, 41]
]
matriz_rotada = [matriz[columna][fila] for columna in range(len(matriz[0])) for fila in range(len(matriz) - 1, -1, -1)]

print(f"la matriz rotada es:\n")
for fila in matriz_rotada:
    print(f"{fila}\n")

#Actividad N12
cadena_notas = "10,8,100,-5,-6,3,90,95,38,45,68,72,70,110,452,-219,-3000, 55, 24"
lista_notas = [int(nota) for nota in cadena_notas.split(",")]
lista_aprobados = []
lista_desaprobados = []
notas_validas = []

for nota in lista_notas:
    if 0 <= nota <= 100:
        notas_validas.append(nota)
    else:
        continue

for nota in notas_validas:
    if nota >= 60:
        lista_aprobados.append(nota)
    else:
        lista_desaprobados.append(nota)

print(f"las notas aprobadas son: {lista_aprobados} \n")
print(f"las notas desaprobados son: {lista_desaprobados} \n")
print(f"El promedio de las notas validas es: {sum(notas_validas) / len(notas_validas)}\n")
print(f"los ultimos dos aprobados son: {lista_aprobados[-2:]}\n")

#Actividad N13
tareas = []

while True:
    seleccion = input(f"Seleccione una opción:\n1. 1 == Agregar tarea\n2. 2 == Eliminar tarea\n3. 3 == ver Resumen\n4. 4 == Salir\nOpción: ")
    if seleccion == "1":
        tarea = input(f"Ingrese la tarea: \n")
        if tarea in tareas:
            print(f"\nLa tarea : {tarea}  ya está en la lista.")
            continue
        else:
            tareas.append(tarea)
        print("Tarea agregada exitosamente.")
    elif seleccion == "2":
        tarea = input("Ingrese la tarea a eliminar: \n")
        if tarea in tareas:
            tareas.remove(tarea)
            print(f"\nLa Tarea : {tarea} fue eliminada exitosamente.")
        else:
            print(f"\nLa tarea : {tarea} no está en la lista.")
    elif seleccion == "3":
        print(f"el total de tareas registradas es: {len(tareas)}\n")
        print(f"las primeras tres tareas son: {tareas[:3]}\n")
    elif seleccion == "4":
        print("\nSaliendo del programa.\n")
        break
    else:
        print("\nOpción inválida. Por favor, seleccione una opción válida.\n")
        