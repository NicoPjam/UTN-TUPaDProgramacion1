
#Actividad 6

agenda = {
    ("Lunes","Manana"): "Clase de Programación",
    ("Lunes","Tarde"): "Clase de Matemáticas",
    ("Martes","Manana"): "Clase de Sistemas Operativos",
    ("Miercoles","Manana"): "Clase de sistemas Operativos",
    ("Jueves","Manana"): "Clase de Matemáticas",
    ("Viernes","Manana"): "Clase de Organización Empresarial", 
}

def consultar_agenda(dia, hora):
    if (dia, hora) in agenda:
        return agenda[(dia, hora)]
    else:
        return "No hay clase en ese horario"

dia = input("Ingrese el dia de la semana (Lunes, Martes, Miercoles, Jueves, Viernes): ")
hora = input("Ingrese la hora (Manana, Tarde): ")

print(consultar_agenda(dia, hora))