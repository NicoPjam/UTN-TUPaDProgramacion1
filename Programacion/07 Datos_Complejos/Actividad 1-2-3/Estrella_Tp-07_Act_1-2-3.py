#Actividad 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Actividad 2)

precios_frutas['Banana'] = 1300
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Actividad 3)
total_frutas = []

for fruta in precios_frutas:
    total_frutas.append(fruta)
print(total_frutas)
#Forma con .keys
print(f"las frutas son : {precios_frutas.keys()}")

