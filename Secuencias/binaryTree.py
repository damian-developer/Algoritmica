class ADTBinaryTree:

    def num_children(self, p):
        count = 0
        if p.left() is not None:
            count += 1
        if p.right() is not None:
            count += 1
        return count
    
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return self.root() is None
    
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

class BinaryTreeNode:

    def __init__(self, element = None, parent = None, left = None, right = None):
        
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right

    def left(self):
        return self._left
    
    def right(self):
        return self._right
    
    def element(self):
        return self._element
    
    def __str__(self):
        return f"* {self.element()}"

class BinaryTree(ADTBinaryTree):

    def __init__(self):
        self._root = None
        self._size = 0
    
    def root(self):
        return self._root
    
    def parent(self, p):
        return p._parent
    
    def __len__(self):
        return self._size
    
    def left(self, p):
        return p._left
    
    def right(self, p):
        return p._right
    
    def _count_nodes(self, p):
        if p is None:
            return 0
        else:
            return 1 + self._count_nodes(p._left) + self._count_nodes(p._right)

    #Add
    def add_root(self, element):
        if self.root() is not None:
            raise ValueError("El arbol ya posee una raiz")
        
        node = BinaryTreeNode(element)
        self._root = node
        self._size = 1
        return node
    
    def add_left(self, p, element):
        if p._left is not None:
            raise ValueError("El nodo ya posee un hijo")
        
        node = BinaryTreeNode(element)
        p._left = node
        node._parent = p
        self._size += 1
        return node

    def add_right(self, p, element):
        if p._right is not None:
            raise ValueError("El nodo ya posee un hijo")
        
        node = BinaryTreeNode(element)
        p._right = node
        node._parent = p
        self._size += 1
        return node

    def attach(self, p, t1, t2):
        if not self.is_leaf(p):
            raise ValueError("El nodo debe ser una hoja")

        else:
            if not t1.is_empty():
                t1.root()._parent = p
                p._left = t1.root()
                self._size += len(t1)
            if not t2.is_empty():
                t2.root()._parent = p
                p._right = t2.root()
                self._size += len(t2)

    #Recorridos
    def _preorder(self, p):
        if p is not None:
            yield p
            yield from self._preorder(p._left)
            yield from self._preorder(p._right)

    def _postorder(self, p):
        if p is not None:
            yield from self._postorder(p._left)
            yield from self._postorder(p._right)     
            yield p
    
    def _inorder(self, p):
        if p is not None:
            yield from self._inorder(p._left)
            yield p
            yield from self._inorder(p._right)

    def nodes(self, default = _preorder):
        for p in default(self.root()):
            yield p
    
    def __str__(self):
        return self._str_tree(self.root())

    
    def _str_tree(self, p, depth = 0):
        if p is None:
            return ""
        else:
            return " " * depth + str(p) + "\n" + self._str_tree(p._left, depth + 1) + self._str_tree(p._right, depth + 1)

arbol = BinaryTree()

root = arbol.add_root("A")

nodo_b = arbol.add_left(root, "B")
nodo_c = arbol.add_right(root, "C")

nodo_d = arbol.add_left(nodo_b, "D")
nodo_e = arbol.add_right(nodo_b, "E")

nodo_x = arbol.add_left(nodo_e, "X")

print("Arbol 1:")
print(arbol)

try:
    arbol.add_left(nodo_b, "Z")
except ValueError as e:
    print("El nodo ya tiene un child")

print(f"El arbol esta vacio: {arbol.is_empty()}")
print(f"El arbol tiene una len: {len(arbol)}")

arbol2 = BinaryTree()

arbol2.add_root("F")

arbol2.add_left(arbol2.root(), "G")
arbol2.add_right(arbol2.root(), "H")

print("Arbol 2:")
print(arbol2)

arbol3 = BinaryTree()

arbol3.add_root("I")

nodo_y = arbol3.add_left(arbol3.root(), "Y")

print("Arbol 3:")
print(arbol3)

arbol.attach(nodo_d, arbol2, arbol3)

print("Arbol completo")
print(arbol)

print("Recorrido preorder:")
for node in arbol.nodes(arbol._preorder):
    print(node)

print("Recorrido postorder:")
for node in arbol.nodes(arbol._postorder):
    print(node)

print("Recorrido inorder:")
for node in arbol.nodes(arbol._inorder):
    print(node)