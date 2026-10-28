class Articulo:
    def __init__(self, codigo = 0, denominacion = "", precio = 0.0):
        self.codigo = codigo
        self.descripcion = denominacion
        self.precio = precio

    def __str__(self):
        return f"Articulo: {self.descripcion} - Precio: {self.precio} - Codigo: {self.codigo}"