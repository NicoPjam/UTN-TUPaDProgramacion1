from Articulo import Articulo
from RemitoVentaDetalle import RemitoVentaDetalle
from RemitoVenta import RemitoVenta
from RepartoDiario import RepartoDiario
class CrearRepartoDiario:
    @staticmethod
    def main():

        Articulos_disponibles = [
            Articulo(10,"Filtro de aceite", 10000.0),
            Articulo(20,"Filtro de Aire", 8000.0),
            Articulo(30,"Filtro de combustible", 7500.0),
            Articulo(40,"Aceite de Motor sw/10", 25000.0),
            Articulo(50,"Correa de distribucion", 20000.0),
        ]
        clientesReparto = {
            "20284569875": "Juan Alonso",
            "20157896542 ": "Emiliano Salas",
            "50258963654": "Pacallcar Autos",
            "27654987456": "Julieta Videla",
            "50335588945": "Todo Auto SRL",
        }

        print(f"=== Gestion de Reparto Diario ===")
        while (True):
            print("Ingrese los datos de la fecha del reparto: ")
            try:
                dia = int(input("Dia: "))
                if dia < 1 or dia > 31:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Error: Ingrese un valor numérico para el dia entre 1 y 31.")
                continue
        while (True):
                    print("Ingrese los datos de la fecha del reparto: ")
                    try:
                        Mes = int(input("Mes: "))
                        if Mes < 1 or Mes > 12:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Error: Ingrese un valor numérico para el Mes entre 1 y 12.")
                        continue
        while (True):
                    print("Ingrese los datos de la fecha del reparto: ")
                    try:
                        anio = int(input("Año: "))
                        if anio < 1900 or anio > 2023:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Error: Ingrese un valor numérico para el dia entre 1 y 31.")
                        continue
        fecha_reparto = f"{dia}/{Mes}/{anio}"
        reparto = RepartoDiario(fecha_reparto)

        remitos_ventas = []

        while True:
            print("\nIngrese los datos del remito de venta:")
            try:
                cuit_cliente = int(input("Cuit del cliente: "))
                if len(str(cuit_cliente)) != 11:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Error: Ingrese un CUIT valido.")
                continue
            if cuit_cliente not in clientesReparto:
                while True:
                    nombre_cliente = input("no se encontro un Cuit. Ingrese el nombre del cliente: ")
                    if nombre_cliente == "":
                        print("Error: Ingrese un nombre valido.")
                        continue
                    elif not nombre_cliente.isalpha():
                        print("Error: Ingrese un nombre valido.")
                        continue
                    else:
                        break
                clientesReparto[cuit_cliente] = nombre_cliente
            break

        while True:
            print("que articulo desea ingresar?")
            for articulo in Articulos_disponibles:
                print(f"{articulo}")
            try:
                codigo_articulo = int(input("Ingrese el codigo del articulo: "))
                if not any(articulo.codigo == codigo_articulo for articulo in Articulos_disponibles):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Error: Ingrese un Codigo valido.")
                continue

        while True:
            try:
                cantidad_articulo = int(input("Ingrese la cantidad de articulos: "))
                if cantidad_articulo < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Error: Ingrese una cantidad valida.")
                continue

        for articulo in Articulos_disponibles:
            if articulo.codigo == codigo_articulo:
                remito_venta = RemitoVenta(cuit_cliente, clientesReparto[RemitoVentaDetalle(cantidad_articulo, articulo)], fecha_reparto)
        
if __name__ == "__main__":
    while True:
        CrearRepartoDiario.main()