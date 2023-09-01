class _DoublyLinkedBase:
    """Una base de clase que implementa una lista enlazada doble."""

    class _Node:
        """Nodo ligado a otros nodos con referencias a los nodos previos y siguientes."""

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

        def __str__(self):
            return str(self._element)
            
    
    def __init__(self):
        """Crea una lista enlazada doble vacía."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Devuelve el número de elementos en la lista enlazada doble."""
        return self._size

    def is_empty(self):
        """Devuelve True si la lista enlazada doble está vacía."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Añade un elemento entre dos nodos existentes y devuelve el nuevo nodo."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Elimina un nodo de la lista y devuelve su elemento."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    ##adaptar
    def _busca_nodo(self, posicion):
        if posicion < 0 or posicion > self._tamaño:
            raise IndexError("Posición inválida")

        actual = self._header._siguiente
        for _ in range(posicion):
            actual = actual._siguiente
        self._borrar_elemento(actual)