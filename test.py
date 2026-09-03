def OperacionesBasicasAB(a, b):
    resultado = (a + b, a - b, a * b, a / b)
    return resultado
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

print("el resultado de la suma es: ", OperacionesBasicasAB(a, b)[0])
print("el resultado de la resta es: ", OperacionesBasicasAB(a, b)[1])
print("el resultado de la multiplicacion es: ", OperacionesBasicasAB(a, b)[2])
print("el resultado de la division es: ", OperacionesBasicasAB(a, b)[3])
