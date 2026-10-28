from Functions import *
matriz = Matriz()

while True:
    print("\nBienvenido al programa de ingreso de celdas.")
    print("Ingrese FIN como valor para finalizar.")

    valor = input("Ingrese un valor para la celda: ").strip()

    if valor.upper() == "FIN":
        print("Finalizando el programa. Gracias por usarlo.")
        print("Las celdas ingresadas son:")
        print("Fila\tColumna\tValor")
        matriz.mostrarMatriz()
        break

    elif valor == "":
        print("Valor inválido. No puede ingresar un valor vacío.")
        continue

    while True:
        print("Ingrese la posición de la celda:")
        fila = input("Fila: ").strip()
        columna = input("Columna: ").strip()

        if fila == "" or columna == "":
            print("Error: no puede ingresar valores vacíos.")

        elif not fila.isdigit() or not columna.isdigit():
            print("Error: debe ingresar números enteros.")

        elif int(fila) < 1 or int(columna) < 1:
            print("Error: la fila y la columna deben ser mayores que cero.")

        else:
            fila = int(fila)
            columna = int(columna)
            break

    nueva_celda = Celdas(fila, columna, valor)

    if matriz.agregarCelda(nueva_celda):
        print(
            f"Celda ingresada: Fila {fila}, "
            f"Columna {columna}, Valor '{valor}'"
        )
    else:
        print(
            f"Error: ya existe una celda en la posición "
            f"Fila {fila}, Columna {columna}."
        )