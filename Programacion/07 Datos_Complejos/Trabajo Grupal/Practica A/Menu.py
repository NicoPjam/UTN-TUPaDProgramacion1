import Funciones as f
class Menu:
    @staticmethod
    def Inicio():
        print(f"Bienvenido al menu de la maquina de golosinas! A continuacion, ingrese el numero correspondiente a la accion que desea realizar: \n")
        print(f"1. Pedir golosina\n2. Mostrar golosinas\n3. Recargar golosinas 4. Salir\n")
    @staticmethod
    def procesarOpcion(opcion):
        if opcion == "1":
            f.Funciones.pedirGolosinas()
        elif opcion == "2":
            f.Funciones.mostrarGolosinas()
        elif opcion == "3":
            f.Funciones.recargarGolosinas()
        elif opcion == "4":
            f.Funciones.apagarMaquina()
        else:
            print("Opcion no valida")

while True:
    Menu.Inicio()
    opcion = input("Ingrese una opcion: ")
    Menu.procesarOpcion(opcion)