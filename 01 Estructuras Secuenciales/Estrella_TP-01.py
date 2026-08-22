#Trabajo Practico N1 Secuenciales UTN Programación

#Actividad N1

print("Hola Mundo!")

#Actividad N2

nombre = input("Ingrese su Nombre! : ")
print(f"Hola! {nombre}, que tal? \n")

#Actividad N3

nombre = input("Ingrese su Nombre! : ")
apellido = input("Ingrese su Apellido! : ")
edad = input("Ingrese su Edad! : ")
pais = input("Ingrese su Pais de Origen! : ")
print(f"Yo soy {nombre} {apellido}, tengo {edad} y soy de {pais}\n")

#Actividad N4

Pi = 3.14
radio = float(input("ingrese el radio del circulo! : "))

area = Pi * (radio ** 2)
perimetro = 2 * Pi * radio

print(f"El Area del circulo con radio {radio} es {area:.2f} y el perimetro {perimetro:.2f}\n")

#Actividad N5

segundos = int(input("Ingrese la cantidad de segundos en enteros a transformar: "))
horas = segundos / 3600 
print(f"La cantidad de segundos {segundos} es equivalente a {horas} Hs!! \n")

#Actividad N6

numero = int(input("ingrese un numero entero para ver su tabla de multiplicacion!! : "))

print(f"La tabla de Multiplicacion de {numero} es : ")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10} \n")

#Actividad N7

num1 = int(input("ingrese el primer numero entero distinto de 0! : "))
num2 = int(input("ingrese el segundo numero entero distinto de 0! : "))

print(f"Estos son los resultados de : ")
print(f"La suma entre {num1} y {num2} = {num1 + num2}")
print(f"La resta entre {num1} y {num2} = {num1 - num2}")
print(f"La multiplicacion entre {num1} y {num2} = {num1 * num2}")
print(f"La division entre {num1} y {num2} = {num1 / num2} \n")

#Actividad N8

peso= float(input("ingrese su peso corporal en kg: "))
altura= float(input("ingrese su altura en metros: "))
imc = peso / (altura ** 2)    
print(f"tu indice de masa corporal segun tu peso {peso}kg y tu altura {altura}m es! {imc:.2f} \n")

#Actividad N9

temperaturaC = float(input("ingrese a continuacion la temperatura en Grados Celcius, que desea transformar! : "))
conversionF = (9 / 5) * temperaturaC + 32
print(f"La temperatura en Grados Celsius: {temperaturaC} es equivalente a {conversionF} Grados Fahrenheit \n")

#Actividad N10

num1 = int(input("Ingrese el primer numero! : "))
num2 = int(input("Ingrese el segundo numero! : "))
num3 = int(input("Ingrese el tercer numero! : "))
promedio = (num1 + num2 + num3) / 3
print(f"el resultado del promedio entre los numeros {num1}, {num2}, {num3} es igual a : {promedio}")
