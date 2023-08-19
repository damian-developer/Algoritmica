class Node:
    def __init__(self, element, parent=None, children=None):
        self._element = element
        self._parent = parent
        if children is None:
            self._children = []
        else:
            self._children = children
    
    def element(self):
        return self._element

    def add(self, element):
        element = Node(element)
        if element not in self._children:
            element._parent = self
            self._children.append(element)
            return element
        else:
            raise ValueError("El nodo tiene un padre")

    def __len__(self):
        return self._size
    
    def __str__(self):
        return f"* {self.element()}"

class ADTTree:
    def __init__(self, root=None):
        self._size = 0
        if root is not None:
            self.add_root(root)
        else:
            self._root = None

    def add_root(self, element):
        if not self.is_empty():
            raise ValueError("El arbol ya tiene una raiz")
        self._root = Node(element)
        self._size += 1

    def is_empty(self):
        if self.root() is None:
            return True
        else:
            return False
    
    def root(self):
        return self._root

    def is_root(self, p):
        return p == self.root()

    def parent(self, p):
        return p._parent

    def children(self, p):
        for child in p._children:
            yield child
    
    def is_leaf(self, p):
        if self.num_children(p) > 0:
            return False
        else:
            return True
    
    def num_children(self, p):
        return len(p._children)

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height_recursive(p)

    def _height_recursive(self, p):
        if self.is_leaf(p):
            return 0
        else:
            heights = []
            for child in self.children(p):
                heights.append(self.height(child))
            return 1 + max(heights)

    def __len__(self):
        return self._size
    
    def __str__(self):
        return self._str_recursive(self._root)
    
    def _str_recursive(self, node, depth=0):
        resultado = "  " * depth + str(node) + "\n"

        for child in node._children:
            resultado += self._str_recursive(child, depth + 1)
        return resultado 

arbol = ADTTree()

#raiz
arbol.add_root("A")

nodo_b = arbol._root.add("B")
nodo_c = arbol._root.add("C")

nodo_d = nodo_b.add("D")
nodo_e = nodo_b.add("E")

nodo_f = nodo_d.add("F")

print(arbol)
print(f"Cantidad de nodo: {len(arbol)}")

print(f"Padre de root: {arbol.parent(arbol.root())}")

print(f"Cantidad de hijos de D: {arbol.num_children(nodo_d)}")
print(f"Cantidad de hijos de B: {arbol.num_children(nodo_b)} \n")

print("Hijos de B:")
for child in arbol.children(nodo_b):
    print(child)

print("Profundidad")
print(f"Raiz: {arbol.depth(arbol.root())}")
print(f"{nodo_b}: {arbol.depth(nodo_b)}")


print("Altura")
print(f"Raiz: {arbol.height(arbol.root())}")
print(f"{nodo_d}: {arbol.height(nodo_d)}")
