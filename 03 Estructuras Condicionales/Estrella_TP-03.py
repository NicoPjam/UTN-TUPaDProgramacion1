#Trabajo Practico N1 Secuenciales UTN Programación

#Actividad N1

edad_usuario = int(input("Ingrese su edad! : "))
if edad_usuario >= 18:
    print("usted es mayor de edad!\n") 
#Actividad N2

nota = int(input("Ingrese su nota final! : "))
if nota >= 6:
    print("usted esta aprobado!\n")
else:
    print("usted esta desaprobado!\n")

#Actividad N3

numero_ingresado = int(input("ingrese un numero par! : "))
if numero_ingresado % 2 == 0:
    print("Ha ingresado un numero par!\n")
else:
    print("Ese no es un numero par!, Por favor ingrese un numero par!\n")

#Actividad N4

edad_usuario = int(input("Ingrese su edad! : "))
if edad_usuario < 12:
    print("eres un/a niño/a!\n")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("eres un adolescente!\n")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("eres un/a adulto/a joven!\n")
else:
    print("eres un/a Adulto/a!\n")

#Actividad N5

contraseña = input("Ingrese su contraseña! : ")
if len(contraseña) <= 14 and len(contraseña) >= 8:
    print("contraseña correctamente ingresada! \n")
else:
    print("debe ingresar una contraseña valida! \n")

#Actividad N6

from statistics import mode,mean,median
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("El Sesgo es positivo! \n")
elif media < mediana and mediana < moda:
    print("El Sesgo es Negativo! \n")
elif media == mediana and mediana == moda:
    print("No hay sesgo")
else:
    print("No se puede determinar el sesgo")

#Actividad N7

frase = input("Ingrese una frase! : ")
if frase[-1] in "aeiouAEIOU":
    print(f"{frase}! \n")
else:
    print(f"{frase}\n")

#Actividad N8
nombre_usuario = input("Ingrese su nombre! : ")
opcion = int(input(f"Hola! {nombre_usuario} \ningresa un valor segun la opcion que desees elegir!\n 1 : Si quiere su nombre en mayúsculas \n 2 : Si quiere su nombre en  Si quiere su nombre en minúsculas. \n 3 : Si quiere su nombre con la primera letra mayúscula \n"))
if opcion == 1:
    print(f"{nombre_usuario.upper()}\n")
elif opcion == 2:
    print(f"{nombre_usuario.lower()}\n")
elif opcion == 3:
    print(f"{nombre_usuario.title()}\n")
else:
    print("opcion invalida! \n")
#Actividad N9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad N10

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if hemisferio == "N":
    
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        print("Otoño")
    else:
        print("Fecha inválida")

elif hemisferio == "S":
    
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        print("Primavera")
    else:
        print("Fecha inválida")

else:
    print("Hemisferio inválido")

