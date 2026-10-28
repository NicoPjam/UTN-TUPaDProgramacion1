from Articulo import Articulo
class RemitoVentaDetalle:
    def __init__(self, cantidad = 0, articulo = Articulo):
        self.cantidad = cantidad
        self.articulo = articulo
    @property
    def SubTotal(self) -> float:
        return self.cantidad * self.articulo.precio

