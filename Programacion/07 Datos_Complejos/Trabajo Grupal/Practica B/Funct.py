class Elementos:
    @staticmethod
    def validarNota(entrada_str: str) -> bool:
        cadena = entrada_str.strip()
        if len(cadena) == 0:
            return False
        puntos = 0
        es_valido = True

        for caracter in cadena:
            if caracter == ".":
                puntos += 1
            elif not caracter.isnumeric():
                es_valido = False

        if es_valido and puntos <= 1:
            valor= float(cadena)
            if 0 <= valor <= 10:
                return True
        return False
    @staticmethod
    def solicitar_nota(mensaje):
        nota = input(mensaje)
        while not Elementos.validarNota(nota):
            print("La nota ingresada no es válida. Por favor, ingrese una nota válida.")
            nota = input("Ingrese la nota que desea ingresar del rango (0-10): ")
        return float(nota)