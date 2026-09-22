import os

productos = {}
class Funciones:
    @staticmethod
    def cargarProductos():
        if not os.path.exists("productos.txt"):
            with open(r"productos.txt", "w") as archivo:
                pass
        else:
            with open(r"productos.txt", "r") as archivo:
                for linea in archivo:
                    producto = linea.strip().split(";")
                    productos[producto[0]] = [producto[1], producto[2]]
    @staticmethod
    def MostrarProductos():
        if len(productos) == 0:
            print("No hay productos cargados")
            return
        for producto in productos:
            if int(productos[producto][1]) > 0:
                print(f"Producto: {producto}, Precio: {productos[producto][0]}, Cantidad: {productos[producto][1]}")
            else:
                print(f"Producto: {producto}, Precio: {productos[producto][0]}, Agotado")
    @staticmethod
    def AgregarProducto(producto, precio, cantidad):
        if productos == {}:
            Funciones.cargarProductos()
        if producto in productos:
            productos[producto][0] = precio
            productos[producto][1] = cantidad
        else:
            productos[producto] = [precio, cantidad]

    @staticmethod
    def GuardarProductos():
        if productos == {}:
            Funciones.cargarProductos()
        with open(r"productos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"{producto},{productos[producto][0]},{productos[producto][1]}\n")
        
