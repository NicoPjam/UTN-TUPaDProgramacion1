
from Funciones import *
class Menu: 
    @staticmethod
    def inicio():
        while True:
            print(f"Hola Bienvenido al registro de alumnos de la UTN")
            print("Seleccione la opcion que desea realizar: !")
            print("╔══════════════════════════════╗")
            print("║ 1. ver Alumnos               ║")
            print("║ 2. Agregar Alumnos           ║")
            print("║ 3. Generar Informe Aprobados ║")
            print("║ 4. Salir                     ║")
            print("╚══════════════════════════════╝")

            opcion = input(f"Seleccione una opcion: ").strip()
            if opcion.isdigit() == False and opcion.isalpha() == True and opcion.isnumeric() == False:
                print(f"La opcion ingresada no es valida. Por favor ingrese una opcion valida.")
                continue
            if int(opcion) < 1 or int(opcion) > 4:
                print(f"La opcion ingresada no es valida. Por favor ingrese una opcion entre 1 y 4.")
                continue
            else:
                if int(opcion) == 1:
                    print("Los Alumnos son: ")
                    Funciones.leer_alumnos()
                elif int(opcion) == 2:
                    Funciones.agregar_alumno()
                elif int(opcion) == 3:
                    Funciones.guardar_aprobados()
                elif int(opcion) == 4:
                    print("Salir")
                    break
            

menu = Menu
menu.inicio()