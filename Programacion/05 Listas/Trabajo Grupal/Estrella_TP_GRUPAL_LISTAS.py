#Actividad N1

lista = (int(x) for x in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(","))
print(f"la suma de la lista es: {sum(lista)}")

#Actividad N2

lista = [int(x) for x in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
maximo = 0
minimo = 0
for i in range(len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
    elif lista[i] < minimo:
        minimo = lista[i]
print(f"El mayor numero de la lista : {lista} \nEs :  {maximo} \nY el minimo \nEs : {minimo}")

#Actividad N3

lista = [str(palabra) for palabra in input("Ingrese una lista de elementos separados por coma sin espacios ! : \n").split(",")]
for elemento in range(len(lista)):
    lista[elemento] = lista[elemento][::-1]
print(f"la lista revertida es: {lista}")

#Actividad N4

lista = [int(numero) for numero in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
contador_par = 0
contador_impar = 0
for numero in lista:
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
print(f"la cantidad de numeros pares es: {contador_par} \nY la cantidad de numeros impares es: {contador_impar}\n")

#Actividad N5

lista = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
multiplicador = int(input(f"Ingrese un numero por el que desea multiplicar la lista! \n {lista}\n : "))
for numero in range(len(lista)):
    lista[numero] = lista[numero] * multiplicador
print(f"La nueva lista es: {lista}\n")

#Actividad N6

lista = [int(numero) for numero in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
sin_repetidos = []
for numero in lista:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)
print(f"la lista sin repetidos es: {sin_repetidos}\n")

#Actividad N7

lista = [int(numero) for numero in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
print(f"el promedio de la lista es: {sum(lista) / len(lista)}\n")

#Actividad N8

lista = [str(elemento) for elemento in input("Ingrese una lista de elementos separados por coma sin espacios ! : \n").split(",")]

elementos_unicos = []
lista_repetidos = []
for elemento in lista:
    if elemento not in elementos_unicos:
        elementos_unicos.append(elemento)
    elif elemento in elementos_unicos and elemento not in lista_repetidos:
        lista_repetidos.append(elemento)
    else:
        pass
print(f"\nlos elementos unicos de la lista : {lista} \nSon: {elementos_unicos}\n")
print(f"los elementos repetidos de la lista Son: {lista_repetidos}\n")

#Actividad N9

lista = [int(numero) for numero in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
Primo = []

for numero in lista:
    if numero > 1:
        for divisor in range(2, numero):
            if (numero % divisor) == 0:
                break
        else:
            Primo.append(numero)


print(f"los numeros primos de la lista son: {Primo}\n")

#Actividad N10

lista = [int(numero) for numero in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
indice = int(input("Ingrese el indice del elemento que desea eliminar! empezando por 1: "))
lista.pop(indice - 1)
print(f"la nueva lista es: {lista}\n")

#Actividad N11

lista = [int(numero) for numero in input("Ingrese una lista de numeros separados por coma sin espacios ! : \n").split(",")]
numero = int(input("Ingrese el numero que desea buscar! : "))

ocurrencias = lista.count(numero)

if ocurrencias > 0:
    print(f"El numero {numero} aparece {ocurrencias} veces en la lista")
else:
    print(f"El numero {numero} no aparece en la lista")

#Actividad N12

lista = [10,22,33,44,55,102,38,40]
lista2 = [11,36,47,58,69,80,91,100]
resultado_suma = []

for elemento in range(len(lista)):
    resultado_suma.append(lista[elemento] + lista2[elemento])
print(f"la suma de los elementos de la lista : \n {lista} \nCon la lista : \n {lista2} \nEs: \n {resultado_suma} \n")

#Actividad N13
print(f"Numpy es una libreria de python que se utiliza para trabajar con matrices matematicamente de forma rapida, eficiente y versatil.\n")
#ejemplo de uso

#import numpy as np !importamos la libreria
#matriz = np.array([[1,2,3],[4,5,6],[7,8,9]]) !creamos la matriz
#print(matriz) !imprimimos la matriz