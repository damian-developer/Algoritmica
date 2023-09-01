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

class Position:
    def __init__(self, container, node):
        self._container = container
        self._node = node
    
    def element(self):
        return self._node._element
    
    def __repr__(self):
        return f"Posición {self.element()}"


class PositionalList(_DoublyLinkedBase):
    def _validate(self, p):
        if not isinstance(p, Position):
            raise TypeError("El valor P debe ser del tipo Posición")
        if p._container is not self:
            raise ValueError("El valor P no pertenece al contenedor")
        if p._node._next is None:
            raise ValueError("La posición no es valida")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return Position(self, node)
    
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor
            cursor = self.after(cursor)
    
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        pass

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
class Vertex:
    def __init__(self, element):
        self.element = element
        self.incidence_collection = PositionalList()
    
    def __str__(self):
        return str(self.element) 

class Edge:
    def __init__(self, u, v, element, directed = True):
        self.u = u
        self.v = v
        self.element = element
        self.directed = directed
    
    def __str__(self):
        if self.directed:
            return f"{self.u} -> {self.v} : {self.element}"
        else:
            return f"{self.u} - {self.v} : {self.element}"


class ADTGraph:
    def __init__(self, directed = False):
        self._directed = directed
        self._vertices = PositionalList()
        self.edges_count = 0
    
    def vertex_count(self):
        return len(self._vertices)
    
    def vertices(self):
        for node in self._vertices:
            yield node.element()

    def edge_count(self):
        return self.edges_count
    
    def edges(self):
        edges_set = set()
        for node in self._vertices:
            vertex = node.element()
            for node2 in vertex.incidence_collection:
                edge = node2.element()
                edges_set.add(edge)
        for edge in edges_set:
            yield edge
    
    def get_edge(self, u, v):
        for node in u.incidence_collection:
            edge = node.element()
            if self._directed and edge.v == v:
                return edge
            elif not self._directed and (edge.u == v or edge.v == v):
                return edge
        return None
    
    def degree(self, v, out = True):
        """Grado"""
        if not self._directed:
            return len(list(self.incident_edges(v)))
        else:
            if out:
                return len(list(self.incident_edges(v)))
            else:
                return len(list(self.incident_edges(v, out = False)))
        
    def incident_edges(self, v, out = True):
        if not self._directed:
            for node in v.incidence_collection:
                yield node.element()
        else:
            for node in v.incidence_collection:
                edge = node.element()
                if out:
                    if edge.u == v:
                        yield edge
                else:
                    if edge.v == v:
                        yield edge
    
    def insert_vertex(self, x = None):
        vertex = Vertex(x)
        self._vertices.add_last(vertex)
        return vertex

    def insert_edge(self, u, v, x = None):
        edge = Edge(u, v, x, self._directed)
        u.incidence_collection.add_last(edge)
        v.incidence_collection.add_last(edge)
        if not self._directed:
            self.edges_count += 1

        return edge


    def remove_vertex():
        pass

    def remove_edge():
        pass

grafo = ADTGraph(directed=True)

v1 = grafo.insert_vertex("A")
v2 = grafo.insert_vertex("B")
v3 = grafo.insert_vertex("C")
v4 = grafo.insert_vertex("D")
v5 = grafo.insert_vertex("E")
v6 = grafo.insert_vertex("F")

grafo.insert_edge(v1, v2, "Arista 1")
grafo.insert_edge(v2, v3, "Arista 2")
grafo.insert_edge(v3, v1, "Arista 3")
grafo.insert_edge(v4, v5, "Arista 4")
grafo.insert_edge(v5, v6, "Arista 5")

print("Los vertices del grafo son :")
for vertex in grafo.vertices():
    print(vertex)


print("Las aristas del grafo son :")
for edge in grafo.edges():
    print(edge)

print(f"Las aristas incidentes desde el vertice {v1} son :")
for edge in grafo.incident_edges(v1):
    print(edge)

print(f"la cantidad de aristas del grafo son: {grafo.edge_count()}")

print(f"la cantidad de vertices son: {grafo.vertex_count()}")

print(f"La arista que conecta los vertices {v1} y {v2} es: {grafo.get_edge(v1, v2)}")
print(f"La arista que conecta los vertices {v3} y {v1} es: {grafo.get_edge(v3, v1)}")