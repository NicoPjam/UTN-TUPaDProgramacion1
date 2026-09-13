#Actividad N1

numeros = []
for i in range(1,100):
    if i % 4 == 0:
        numeros.append(i)
print(f"Los numeros multiplos de 4 entre 1 y 100 son: {numeros} \n")

#Actividad N2

lista = ["Half_life","Counter_Strike","Black_Mesa","Oppossing_Force","Blue_Shift"]
print(f"el penultimo juego de la lista es: {lista[-2]} \n")

#Actividad N3

lista_palabras = []
for i in range(3):
    palabra = input("Ingrese una palabra! : ")
    lista_palabras.append(palabra)
print(f"las palabras ingresadas son: {lista_palabras} \n")

#Actividad N4

animales = ["perro", "gato", "conejo", "pez"]
print(f"los animales son: {animales} \n")
animales [1] = "loro"
animales [3] = "oso"
print(f"ahora los animales son: {animales} \n")

#Actividad N5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(f"los numeros son: {numeros} \n")
#El codigo consta de una lista de numeros de los cuales remueve el valor maximo mediante el uso de la funcion remove y el uso de la funcion max para obtener el valor maximo de la lista y borrarlo
#luego imprime la lista resultante

#Actividad N6

nums = []
for i in range(10,30,5):
    nums.append(i)
print(f"los numeros son: {nums[0]} y {nums[1]} \n")

#Actividad N7

autos = ["sedan", "polo", "suran", "gol"]
autos [1] = "mazda"
autos [2] = "toyota"
print(f"los autos son: {autos} \n")

#Actividad N8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(f"los dobles son: {dobles} \n")

#Actividad N9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras [2].append("jugo")
compras [1][1] = "tallarines"
compras [0].remove("pan")

print(f"las compras del primer cliente son: {compras[0]}")
print(f"las compras del segundo cliente son: {compras[1]}")
print(f"las compras del tercer cliente son: {compras[2]} \n")
#Actividad N10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(f"los valores de la lista son: {lista_anidada} \n")