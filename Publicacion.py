class Publicacion():
    def __init__(self, codigo, tema, titulo):
        self.__codigo = int(codigo)
        self.__tema = tema
        self.__titulo = titulo
        self.__prestado = False
    
    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getTema(self):
        return self.__tema

    def setTema(self, tema):
        self.__tema = tema

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def Estado(self):
        if self.__prestado == True:
            print('Prestado')
        else:
            print('Disponible')
        
    def getEstado(self):
        return self.__prestado

    def Prestar(self):
        if self.__prestado == True:
            print('El libro no esta disponible para ser prestado')
        else:
            self.__prestado = False
            print('El libro fue prestado exitosamente')

    def Devolver(self):
        if self.__prestado == True:
            self.__prestado = False
            print('El libro fue devuelto exitosamente')
        else:
            print('El libro esta actualmente disponible, por lo cual no puede ser')
        

    def Muestra(self):
        print('Codigo: ', self.__codigo)
        print('Tema: ', self.__tema)
        print('Titulo: ', self.__titulo)
        print('Estado del libro: ', self.Estado())

    