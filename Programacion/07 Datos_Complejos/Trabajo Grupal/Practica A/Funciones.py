from DataManager import *
class Funciones:
    @staticmethod
    def pedirGolosinas():
        legajo = input("Ingrese el legajo: ")
        if legajo.isdigit() and len(legajo) == 4 and int(legajo) in Empleados:
            print (f"Bienvenido!! Empleado {Empleados[int(legajo)]}")
        else:
            print("Error se introdujo un legajo incorrecto o invalido Recuerde que el legajo debe ser un numero Entero de 4 digitos")
            return 

        while True:
            codigo = input("Ingrese el codigo de la golosina o salir para terminar!!: ")
            if codigo.lower() == "salir":
                print ("Regresando al menu principal!!")
                break
            if not codigo.isdigit():
                print("Error se introdujo un codigo incorrecto o invalido Recuerde que el codigo debe ser un numero Entero")
                continue
            codigo = int(codigo)    
            golosina_encontrada = None
            for golosina in Golosinas:
                if golosina[0] == codigo:
                    golosina_encontrada = golosina
                    break
            if golosina_encontrada is None:
                print(f"No se encontro una golosina con el codigo {codigo}")
                break
            nombre_golosina = golosina_encontrada[1]
            stock_actual = golosina_encontrada[2]
            cantidad = input("Ingrese la cantidad de golosinas a pedir: ")
            if not cantidad.isdigit():
                print("Error se introdujo una cantidad incorrecta o invalida Recuerde que la cantidad debe ser un numero Entero")
                break
            cantidad = int(cantidad)
            if stock_actual < cantidad or stock_actual <= 0:
                print(f"Lo sentimos, la golosina {nombre_golosina} esta agotada")
                stock_actual = 0
                break
            golosina_encontrada[2] -= cantidad
            print(f"Se le ha entregado: {nombre_golosina}.")
            encontrado_en_pedidas = False
            for pedido in Golosinas_Pedidas:
                if pedido[0] == codigo:
                    pedido[2] += cantidad  # Incrementar cantidad pedida
                    encontrado_en_pedidas = True
                    break
            if not encontrado_en_pedidas:
                Golosinas_Pedidas.append([codigo, nombre_golosina, cantidad])

    @staticmethod
    def mostrarGolosinas():
        print("\n--- INVENTARIO DE GOLOSINAS ---")
        for golosina in Golosinas:
            print(f"Código: {golosina[0]}, Nombre: {golosina[1]}, Stock: {golosina[2]}")
        print("\n--- PEDIDOS DE GOLOSINAS ---")
        total_vendidas = 0
        for golosina in Golosinas_Pedidas:
            print(f"Código: {golosina[0]}, Nombre: {golosina[1]}, Total Pedido: {golosina[2]}")
            total_vendidas += golosina[2]                
        print(f"Total de golosinas vendidas: {total_vendidas}")

    @staticmethod
    def recargarGolosinas():
        print("\n--- AUTENTICACIÓN TÉCNICO ---")
        print(f"Por favor, ingrese las 3 contraseñas para acceder al menu de recarga de golosinas: ")
        pass1 = input("Ingrese la primera contraseña: ")
        pass2 = input("Ingrese la segunda contraseña: ")
        pass3 = input("Ingrese la tercera contraseña: ")

        if (pass1,pass2,pass3) != Claves_Tecnico:
            print("Error al ingresar las contraseñas. Acceso denegado.")
            return
        print("\n--- Acceso concedido ---")
        print("\n--- MENU DE RECARGA DE GOLOSINAS ---")
        codigo = input("Ingrese el codigo de la golosina: ")

        if not codigo.isdigit():
            print("Error se introdujo un codigo incorrecto o invalido Recuerde que el codigo debe ser un numero Entero")
            return
        
        codigo = int(codigo)
        golosina_encontrada = None

        for golosina in Golosinas:
            if golosina[0] == codigo:
                golosina_encontrada = golosina
                break
        if golosina_encontrada is None:
            print(f"No se encontro una golosina con el codigo {codigo}")
            return
        cantidad = input("Ingrese la cantidad de golosinas a recargar: ")

        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Error se introdujo una cantidad incorrecta o invalida Recuerde que la cantidad debe ser un numero Entero y mayor a 0")
            return
        
        cantidad = int(cantidad)
        golosina_encontrada[2] += cantidad
        print(f"Se han recargado {cantidad} golosinas de {golosina_encontrada[1]}")
    @staticmethod
    def apagarMaquina():
        print("\n==========================================")
        print("      REPORTE FINAL DE GOLOSINAS PEDIDAS  ")
        print("==========================================")

        if not Golosinas_Pedidas:
            print("No se han realizado pedidos de golosinas.")
        else:
            print("\n--- PEDIDOS DE GOLOSINAS ---")
            for golosina in Golosinas_Pedidas:
                print(f"Código: {golosina[0]}, Nombre: {golosina[1]}, Total Pedido: {golosina[2]}")
                total_acumulado += golosina[2]
            print(f"Total de golosinas vendidas: {total_acumulado}")
        


