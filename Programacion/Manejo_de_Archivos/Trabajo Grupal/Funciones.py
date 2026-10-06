import os

alumnos = {}
aprobados = {}
directorio_relativo = r"Programacion\Manejo_de_Archivos\Trabajo Grupal\Informes_Generados"
ruta_alumnos = os.path.join(directorio_relativo, "alumnos.txt")
ruta_aprobado = os.path.join(directorio_relativo, "aprobados.txt")
class Funciones:

    @staticmethod
    def leer_alumnos():
        if not os.path.exists(directorio_relativo):
            os.makedirs(directorio_relativo, exist_ok=True)
        if not os.path.exists(ruta_alumnos):
            with open(ruta_alumnos, "w") as archivo:
                pass
        else:
            with open(ruta_alumnos, "r") as archivo:
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
        print("══════════════════════════════")
    @staticmethod
    def validar_Nombre_alumno(nombre=""):
        if not nombre.replace(" ", "").isalpha():
            print("El nombre debe contener solo letras")
            return False
        return True

    @staticmethod
    def validar_Apellido_alumno(apellido=""):
        if not apellido.replace(" ", "").isalpha():
            print("El apellido debe contener solo letras")
            return False
        return True

    @staticmethod
    def validar_legajo_alumno(legajo=""):
        if not legajo.isnumeric() or len(legajo) != 5:
            print("El legajo debe ser un número de 5 dígitos")
            return False
        return True

    @staticmethod
    def validar_nota_alumno(nota=""):
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
        while True:
            legajo = input("Ingrese el legajo del alumno: ")
            if Funciones.validar_legajo_alumno(legajo):
                break
        while True:
            nombre = input("Ingrese el nombre del alumno: ")
            if Funciones.validar_Nombre_alumno(nombre):
                break
        while True:
            apellido = input("Ingrese el apellido del alumno: ")
            if Funciones.validar_Apellido_alumno(apellido):
                break
        while True:
            nota = input("Ingrese la nota del alumno: ")
            if Funciones.validar_nota_alumno(nota):
                break
        
        alumnos[legajo] = [nombre, apellido, nota]
        with open(ruta_alumnos, "a") as archivo:
            archivo.write(f"{legajo};{nombre};{apellido};{nota}\n")
        print(f"El alumno {nombre} {apellido} ha sido agregado correctamente")

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
        print("══════════════════════════════")
        with open(ruta_aprobado, "w") as archivo:
            for alumno in aprobados:
                archivo.write(f"{alumno};{aprobados[alumno][0]};{aprobados[alumno][1]};{aprobados[alumno][2]}\n")

