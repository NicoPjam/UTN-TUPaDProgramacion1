#Actividad 5

Frase_Ususario = input("Ingrese una frase! : ")
palabras_unicas = set(Frase_Ususario.split())
for palabra in Frase_Ususario.split():
    print(f"la palabra {palabra} aparece {Frase_Ususario.count(palabra)} veces")
print(f"las palabras unicas son: {palabras_unicas}")
