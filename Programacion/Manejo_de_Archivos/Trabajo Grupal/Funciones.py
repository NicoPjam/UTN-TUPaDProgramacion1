import os

alumnos = {}
aprobados = {}

class Funciones:

    @staticmethod
    def leer_alumnos():
        if not os.path.exists("alumnos.txt"):
            with open(r"alumnos.txt", "w") as archivo:
                pass
        else:
            with open(r"alumnos.txt", "r") as archivo:
                for linea in archivo:
                    alumno = linea.strip().split(";")
                    alumnos[alumno[0]] = [alumno[1], alumno[2], alumno[3]]
        if alumnos == {}:
            print("Lo siento, No hay alumnos cargados")
            return
        print(f"Lista de alumnos:")
        print("══════════════════════════════")
        print("Legajo || Nombre || Apellido || Nota")
        for alumno in alumnos:
            print(f"{alumno} || {alumnos[alumno][0]} || {alumnos[alumno][1]} || {alumnos[alumno][2]}")

    @staticmethod
    def validar_alumno(nombre, apellido, legajo, nota):
        if not legajo.isnumeric() and len(legajo) != 5:
            print("El legajo debe ser un número de 5 dígitos")
            return False
        if not nombre.isalpha():
            print("El nombre debe contener solo letras")
            return False
        if not apellido.isalpha():
            print("El apellido debe contener solo letras")
            return False
        if not nota.isnumeric():
            print("La nota debe ser un número")
            return False
        elif int(nota) < 0 or int(nota) > 10:
            print("La nota debe estar entre 0 y 10")
            return False
        return True
    @staticmethod
    def existe_alumno(legajo):
        if legajo in alumnos:
            return True
        else:
            return False

    @staticmethod
    def agregar_alumno():
        if not os.path.exists("alumnos.txt"):
            with open(r"alumnos.txt", "w") as archivo:
                pass
        else:
            with open(r"alumnos.txt", "a") as archivo:
                pass
        legajo = input("Ingrese el legajo del alumno: ").strip()
        nombre = input("Ingrese el nombre del alumno: ").strip().title()
        apellido = input("Ingrese el apellido del alumno: ").strip().title()
        nota = input("Ingrese la nota del alumno: ").strip()
        if Funciones.validar_alumno(nombre, apellido, legajo, nota) == True:
            if Funciones.existe_alumno(legajo) == True:
                print("El alumno ya existe")
                return
            alumnos[legajo] = [nombre, apellido, nota]
            with open(r"alumnos.txt", "a") as archivo:
                archivo.write(f"{legajo};{nombre};{apellido};{nota}\n")
            print(f"El alumno {nombre} {apellido} ha sido agregado correctamente")
        else:
            print("El alumno no pudo ser agregado porque no cumple con los requisitos")
    

    @staticmethod
    def guardar_aprobados():
        if alumnos == {}:
                    print("No hay alumnos cargados")
                    return
        for alumno in alumnos:
            if int(alumnos[alumno][2]) >= 6:
                aprobados[alumno] = [alumnos[alumno][0], alumnos[alumno][1], alumnos[alumno][2]]
        if aprobados == {}:
            print("Lo siento, No hay alumnos aprobados")
            return
        print("Los alumnos aprobados han sido guardados en el archivo aprobados.txt")
        print(f"Lista de alumnos aprobados:")
        print("══════════════════════════════")
        print("Legajo || Nombre || Apellido || Nota")
        for alumno in aprobados:
            print(f"{alumno} || {aprobados[alumno][0]} || {aprobados[alumno][1]} || {aprobados[alumno][2]}")
