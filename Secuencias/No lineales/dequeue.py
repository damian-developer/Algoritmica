from listaEnlazadaDoble import _listaEnlazadaDoble

class linkedDequeue(_listaEnlazadaDoble):

    def first(self):
        return self._header._siguiente._elemento
    
    def last(self):
       return self._trailer._previo._elemento

    def insert_first(self, element):
        self._insertar(element, self._header, self._header._siguiente)
    
    def insert_last(self, element):
        self._insertar(element, self._trailer, self._trailer._previo)

    def delete_last(self, nodo):
        self._borrar_elemento(nodo)
    
    def delete_first(self, nodo):
        self._borrar_elemento(nodo)

deck = linkedDequeue()
deck.insert_first(1)
deck.insert_first(2)
deck.insert_first(4)

print(deck.first())
print(deck.last())