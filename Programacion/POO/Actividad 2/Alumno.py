class Alumno:
    def __init__(self, nombre_completo="", legajo=0, notas=None):
        self.nombre_completo = nombre_completo
        self.legajo = legajo
        self.notas = notas if notas is not None else []

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0.0
        suma = sum(nota.notaExamen for nota in self.notas)
        return suma / len(self.notas)