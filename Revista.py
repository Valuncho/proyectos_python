from Publicacion import *

class Revista(Publicacion):
    def __init__(self, codigo, tema, titulo, numero, fecha):
        super().__init__(codigo, tema, titulo)
        self.__numero = int(numero)
        self.__fecha = fecha

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = int(numero)

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha

    
    def Muestra(self):
        super().Muestra()
        print('El numero es: ', self.__numero)
        print('La fecha es: ', self.__fecha)

    