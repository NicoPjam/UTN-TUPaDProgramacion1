from RemitoVentaDetalle import RemitoVentaDetalle

class RemitoVenta :
    def __init__(self, nombreCliente = "", numeroRemito = 0, detallesRemito: list[RemitoVentaDetalle] = None, totalVenta = 0.0) :
        self.nombreCliente = nombreCliente
        self.numeroRemito = numeroRemito
        self.detallesRemito = detallesRemito if detallesRemito is not None else []

    def agregarDetalle(self, detalle: RemitoVentaDetalle) :
        self.detallesRemito.append(detalle)
    @property
    def totalVenta(self) -> float:
        return sum(detalle.subTotal for detalle in self.detallesRemito)
    