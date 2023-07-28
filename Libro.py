from Publicacion import *

class Libro(Publicacion):
    def __init__(self, codigo, tema, titulo, autor):
        super().__init__(codigo, tema, titulo)
        self.__autor = autor

    def getAutor(self):
        return self.__autor

    def setAutor(self, autor):
        self.__autor = autor

    def Muestra(self):
        super().Muestra()
        print('El autor es: ', self.__autor)