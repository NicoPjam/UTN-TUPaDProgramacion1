
#Actividad 10

Paises = {
    "Argentina" : "Buenos Aires",
    "Colombia" : "Bogota",
    "Peru" : "Lima",
    "Chile" : "Santiago",
    "Uruguay" : "Montevideo"
}
invertir = {valor: clave for clave, valor in Paises.items()}
print(invertir)