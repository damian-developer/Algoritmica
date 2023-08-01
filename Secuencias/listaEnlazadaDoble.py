class _listaEnlazadaDoble:

    class _Nodo:
        def __init__(self, elemento, previo, siguiente):
            self._elemento = elemento
            self._previo = previo
            self._siguiente = siguiente
    
    def __init__(self):
        self._header = self._Nodo(None,None,None)
        self._trailer = self._Nodo(None,None,None)
        self._header._siguiente = self._trailer
        self._trailer._previo = self._header
        self._tamaño = 0

    def _insertar(self, elemento, predecesor, sucesor):
        nuevo = self._Nodo(elemento, predecesor, sucesor)
        predecesor._siguiente = nuevo
        sucesor._previo = nuevo
        self._tamaño += 1
        return nuevo

    def _insertar_posicion(self, posicion, elemento):
        if posicion < 0 or posicion > self._tamaño:
            raise IndexError("Posición inválida")

        if posicion == self._tamaño:
            self._insertar(elemento, self._trailer._previo, self._trailer)
        else:
            actual = self._header._siguiente
            for _ in range(posicion):
                actual = actual._siguiente
                self._insertar(elemento, actual._previo, actual)

    def _imprimir(self):
        actual = self._header._siguiente
        while actual != self._trailer:
            print(actual._elemento, end=" <-> ") 
            actual = actual._siguiente
        print("None")
    
    def _borrar_elemento(self, nodo):
        predecesor = nodo._previo
        sucesor = nodo._siguiente
        predecesor._siguiente = sucesor
        sucesor._previo = predecesor
        self._tamaño -= 1

        elemento = nodo._elemento
        nodo._previo = nodo._siguiente = nodo._elemento = None
        return elemento

    def _busca_nodo(self, posicion):
        if posicion < 0 or posicion > self._tamaño:
            raise IndexError("Posición inválida")

        actual = self._header._siguiente
        for _ in range(posicion):
            actual = actual._siguiente
        self._borrar_elemento(actual)      


class miListaEnlazadaDoble(_listaEnlazadaDoble):
    pass


lista = miListaEnlazadaDoble()
lista._insertar(1, lista._header, lista._trailer)
lista._insertar(3, lista._trailer._previo, lista._trailer)
lista._imprimir()

lista._insertar_posicion(1,2)
lista._imprimir()

lista._busca_nodo(1)
lista._imprimir()