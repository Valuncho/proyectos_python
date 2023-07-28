from Biblioteca import *

def Menu(aux):
    print('Aprete 1 para Crear una publicacion')
    print('Aprete 2 para Borrar una publicacion')
    print('Aprete 3 para Prestar una publicacion')
    print('Aprete 4 para Devolver una publicacion')
    print('Aprete 5 para Mostrar las publicaciones disponibles')
    print('Aprete 6 para Mostrar las publicaciones prestadas')
    aux = int(input('O ingrese 0 para salir\n'))
    if aux == 1:
        biblioteca.crearPublicacion()
    if aux == 2:
        biblioteca.borrarPublicacion()
    if aux == 3:
        biblioteca.PrestarPublicacion()
    if aux == 4:
        biblioteca.devolverPublicacion()
    if aux == 5:
        biblioteca.mostrarDisponibles()
    if aux == 6:
        biblioteca.mostrarPrestados()
    return aux

biblioteca = Biblioteca()
aux = 60
while aux != 0:
    Menu(aux)