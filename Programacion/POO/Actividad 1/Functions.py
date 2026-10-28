class Celdas:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Matriz:
    def __init__(self):
        self.celdas_matriz = []

    def agregarCelda(self, nueva_celda: Celdas):
        for celda in self.celdas_matriz:
            if celda.fila == nueva_celda.fila and celda.columna == nueva_celda.columna:
                return False
        self.celdas_matriz.append(nueva_celda)
        return True

    def  obtenerCelda(self, fila: int, columna: int):
        for celda in self.celdas_matriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
            else:
                return "la celda no es correcta"

    def mostrarMatriz(self):
        if not self.celdas_matriz:
            print("La matriz está vacía")
            return

        # Determinar las dimensiones necesarias
        max_fila = max(celda.fila for celda in self.celdas_matriz)
        max_columna = max(celda.columna for celda in self.celdas_matriz)

        # Recorrer cada posición de la matriz
        for fila in range(1, max_fila + 1):
            for columna in range(1, max_columna + 1):
                valor = ""

                # Buscar si existe una celda en esa posición
                for celda in self.celdas_matriz:
                    if celda.fila == fila and celda.columna == columna:
                        valor = celda.valor
                        break