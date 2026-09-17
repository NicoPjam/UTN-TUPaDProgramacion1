# Actividad 8

Productos = {}

def AgregarProducto(producto, cantidad):
    if producto in Productos:
        Productos[producto] += cantidad
    else:
        Productos[producto] = cantidad

def ConsultarProducto(producto):
    if producto in Productos:
        return Productos[producto]
    else:
        return 0

print("Bienvenido a la tienda")
while True:
    print("\n1. Agregar producto\n2. Consultar producto\n3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        AgregarProducto(producto, cantidad)
    elif opcion == 2:
        producto = input("Ingrese el nombre del producto: ")
        cantidad = ConsultarProducto(producto)
        print(f"La cantidad de {producto} es: {cantidad}")
    elif opcion == 3:
        break