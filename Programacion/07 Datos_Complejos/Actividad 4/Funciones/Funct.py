contactos = {}
class Funciones:
    @staticmethod
    def dato():
        if contactos == {}:
            return False
        else:
            return True
    @staticmethod
    def Guardar(nombre = " ", numero = " "):
        contactos[nombre] = numero
        print("Contacto Guardado")
    @staticmethod
    def consultar(nombre = " ", numero = " "):
        if nombre in contactos:
            print(f"El numero de {nombre} es {contactos[nombre]}")
        else:
            print("El contacto no existe")