from Publicacion import *
from Libro import *
from Revista import *

class Biblioteca():
    def __init__(self):
        self.__ListaPublicaciones = []

    def crearLibros(self):
        print('Estas creando un libro:\n')
        cod = int(input('Ingresa el codigo del libro \t'))
        tema = input('Ingresa el tema del libro \t')
        title = input('Ingresa el titulo del libro \t')
        aut = input('Ingresa el autor del libro \t')
        unLibro = Libro(cod, tema, title, aut)
        return unLibro

    def crearRevista(self):
        print('Estas creando una revista\n')
        cod = int(input('Ingresa el codigo de la revista \t'))
        tema = input('Ingresa el tema de la revista \t')
        title = input('Ingresa el titulo de la revista \t')
        num = int(input('Ingresa el numero \t'))
        fecha = input('Ingresa la fecha \t')
        unaRevista = Revista(cod, tema, title, num, fecha)
        return unaRevista

    def Muestra(self):
        for x in self.__ListaPublicaciones:
            x.Muestra()

    def Menu(self):
        aux = 60
        while aux < 0 or aux > 3:
            print('Presiona 1 para crear un Libro ')
            print('Presiona 2 para crear una Revista ')
            aux = int(input('O presiona 0 para salir \n'))
        return aux

    def crearPublicacion(self):
        opcion = int(self.Menu())
        print(opcion)
        while opcion != 0:
            if opcion == 1:
                self.__ListaPublicaciones.append(self.crearLibros())
            elif opcion == 2:
                self.__ListaPublicaciones.append(self.crearRevista())
            opcion = self.Menu()
        
    def borrarPublicacion(self):
        print(self.Muestra())
        print('Que publicacion desea borrar?')
        aux = int(input('Ingrese el codigo \n'))
        for x in self.__ListaPublicaciones:
            if aux == x.getCodigo():
                self.__ListaPublicaciones.remove(x)
                print('Fue borrada exitosamente')

    def PrestarPublicacion(self):
        print(self.Muestra())
        print('Que publicacion desea tomar prestada? ')
        aux = int(input('Ingrese el codigo\n '))
        for x in self.__ListaPublicaciones:
            if aux == x.getCodigo():
                x.Prestar()

    def devolverPublicacion(self):
        print(self.Muestra())
        print('Que publicacion esta devolviendo?')
        aux = int(input('Ingrese el codigo\n '))
        for x in self.__ListaPublicaciones:
            if aux == x.getCodigo():
                x.Devolver()

    def mostrarDisponibles(self):
        for x in self.__ListaPublicaciones:
            if x.getEstado() == False:
                x.Muestra()

    def mostrarPrestados(self):
        for x in self.__ListaPublicaciones:
            if x.getEstado() == True:
                x.Muestra()