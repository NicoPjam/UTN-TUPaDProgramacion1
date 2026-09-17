from Funciones.Funct import Funciones as f

class main():
    print("Bienvenido al Directorio Telefonico Virtual.\n")
    def inicio():
        print("1. Guardar Contacto.\n2. Consultar Contacto.\n3. Salir.\n")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            nombre = input("Ingrese el Nombre: ")
            numero = input("Ingrese el Numero: ")
            f.Guardar(nombre, numero)
            main.inicio()
        elif opcion == "2":
            if f.dato() == False:
                print("No hay contactos guardados")
                main.inicio()
            else:
                nombre = input("Ingrese el Nombre que quiere consultar: ")
                f.consultar(nombre)
                main.inicio()
        elif opcion == "3":
            print("Saliendo")
        else:
            print("Opcion no valida")
            main.inicio()

main.inicio()
