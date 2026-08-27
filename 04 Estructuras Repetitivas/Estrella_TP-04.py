#Trabajo Practico N1 Secuenciales UTN Programación

#Actividad N1
contador = 0
while contador <= 100:
    print(f"Numero: {contador}")
    contador += 1

#Actividad N2

numero_solicitado = input("\nIngrese un numero entero! : \n")
cont_digitos = 0
for i in range(len(numero_solicitado)):
    cont_digitos += 1
print(f"El numero {numero_solicitado} tiene {cont_digitos} digitos\n")

#Actividad N3

limite_inferior = int(input("Ingrese el limite inferior! : \n"))
limite_superior = int(input("Ingrese el limite superior! : \n"))
for i in range(limite_inferior + 1, limite_superior):
    print(i)

#Actividad N4

detector = True
suma = 0
while detector == True:
    numero = int(input("Ingrese un numero entero! para almacenar en la suma recuerde que si ingresa 0 se detendra! : \n"))
    suma = suma + numero
    if numero == 0:
        detector = False
        print(f"la suma de los numeros ingresados es : {suma}\n")
    else:
        print(f"se sumo el numero {numero} \n")

#Actividad N5

import random
numero_aleatorio = random.radint(0, 9)
acierto = False
while acierto == False:
    numero_ingresado = int(input("Ingrese un numero entero del 0 al 9 y veamos si eres capaz de adivinar! : \n"))
    if numero_ingresado == numero_aleatorio:
        print("Felicidades usted acerto!\n")
        acierto = True
    else:
        print("Vuelva a intentarlo!\n")

#Actividad N6
contador = 100
while contador > 0:
    print(f"Numero: {contador}")
    contador -= 2

#Actividad N7

rango_inferior = 0
rango_superior = int(input("Ingrese el rango max! : \n"))
suma = 0
for i in range(rango_inferior, rango_superior):
    suma = suma + i
print(f"la suma de los numeros entre {rango_inferior} y {rango_superior} es : {suma}\n")

#Actividad N8
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(100):
    valor_ingresado = int(input("Ingrese un numero entero! : \n"))
    if valor_ingresado % 2 == 0:
        pares += 1
    else:
        impares += 1
    if valor_ingresado < 0:
        negativos += 1
    else:
        positivos += 1
print(f"hay {pares} numeros pares \n")
print(f"hay {impares} numeros impares \n")
print(f"hay {negativos} numeros negativos \n")
print(f"hay {positivos} numeros positivos \n")

#Actividad N9

contador = 0
suma = 0

while contador < 100:
    valor_ingresado = int(input("Ingrese un número entero: \n"))
    suma += valor_ingresado
    contador += 1

media = suma / contador

print(f"La media es: {media}\n")

#Actividad N10

numero = input("ingrese un numero! : \n")
numero_invertido = ""
for digito in str(numero):
    numero_invertido = digito + numero_invertido
print(f"el numero invertido es : {numero_invertido}")