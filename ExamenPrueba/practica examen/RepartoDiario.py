from RemitoVenta import RemitoVenta


class RepartoDiario:
    def __init__(self, fecha: str = ""):
        self.fecha = fecha
        self.remitosVenta = []

    def agregarRemito(self, remito: RemitoVenta):
        self.remitosVenta.append(remito)
    @property
    def calcularTotalReparto(self) -> float:
        return sum(remito.totalVenta for remito in self.remitosVenta)