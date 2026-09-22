from Programacion.Manejo_de_Archivos.Tp_Unidad.Funciones import *

while True:
    print("1. Cargar Productos")
    print("2. Mostrar Productos")
    print("3. Agregar Producto")
    print("4. Salir")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        Funciones.cargarProductos()
    elif opcion == "2":
        Funciones.MostrarProductos()
    elif opcion == "3":
        producto = input("Ingrese el nombre del producto: ").title()
        if producto.isdigit():
            print("El nombre del producto no puede ser un numero")
            continue
        precio = input("Ingrese el precio del producto: ")
        if precio.isdigit() == False and int(precio) < 0:
            print("El precio del producto debe ser un numero positivo")
            continue
        cantidad = input("Ingrese la cantidad del producto: ")
        if cantidad.isdigit() == False and int(cantidad) < 0:
            print("La cantidad del producto debe ser un numero positivo")
            continue
        Funciones.AgregarProducto(producto, precio, cantidad)
        Funciones.GuardarProductos()
    elif opcion == "4":
        break