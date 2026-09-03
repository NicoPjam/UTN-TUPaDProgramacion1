#Actividad N1

def LlamarHolaMundo():
    print("hola mundo\n")

LlamarHolaMundo()

#Actividad N2

def SaludarUsuario(nombre):
    print(f"Hola {nombre}! Que tengas un buen dia\n")
nombre = input("Ingrese su nombre: ")
SaludarUsuario(nombre)

#Actividad N3

def InformacionPersonal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}\n")
nombre_Usuario = input("Ingrese su nombre: ")
apellido_Usuario = input("Ingrese su apellido: ")
edad_Usuario = input("Ingrese su edad: ")
direccion_Usuario = input("Ingrese su residencia: ")

InformacionPersonal(nombre_Usuario, apellido_Usuario, edad_Usuario, direccion_Usuario)

#Actividad N4

Pi = 3.1416
def CalcularAreaCirculo(radio):
    global Pi
    area = Pi * (radio**2)
    return area
def CalcularPerimetroCirculo(radio):
    global Pi
    perimetro = 2 * Pi * radio
    return perimetro
radio = float(input("Ingrese el radio del circulo: "))
area = CalcularAreaCirculo(radio)
perimetro = CalcularPerimetroCirculo(radio)
print(f"El area del circulo de radio {radio} es : \n{area} \ny el perimetro es : \n{perimetro} \n")

#Actividad N5
segundos = int(input("Ingrese la cantidad de segundos: "))
def Segundos_a_Horas(segundos):
    horas = segundos // 3600
    return horas
print(f"Los segundos ingresados son : {segundos} y la equivalente cantidad de horas es : {Segundos_a_Horas(segundos)}\n")
#Actividad N6

def TablaDeMultiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Ingrese un numero: "))
print(f"La tabla de multiplicar del numero {num} es : \n")
TablaDeMultiplicar(num)

#Actividad N7

def OperacionesBasicasAB(a, b):
    resultado = (a + b, a - b, a * b, a / b)
    return resultado
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

print("el resultado de la suma es: ", OperacionesBasicasAB(a, b)[0])
print("el resultado de la resta es: ", OperacionesBasicasAB(a, b)[1])
print("el resultado de la multiplicacion es: ", OperacionesBasicasAB(a, b)[2])
print("el resultado de la division es: ", OperacionesBasicasAB(a, b)[3])

#Actividad N8

def CalcularImc(peso, altura):
    imc = peso / (altura**2)
    return imc

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = CalcularImc(peso, altura)
print(f"Su Indice de Masa Corporal segun los datos ingresados es: {imc}")

#Actividad N9

def celciusAFahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

celcius = float(input("Ingrese la temperatura en celcius: "))
fahrenheit = celciusAFahrenheit(celcius)
print(f"La temperatura en fahrenheit es: {fahrenheit}")

#Actividad N10

def CalcularPromedio (a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

print(f"El promedio de los numeros ingresados es: {CalcularPromedio(a, b, c)}")