class Stack:
    def __init__(self):
        self._data = []
     
    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        else:
            raise IndexError('La pila esta vacia')
    
    def top(self):
        if not self.is_empty():
            return self._data[-1]
        else:
            raise IndexError('La pila esta vacia')
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def display(self):
        print("La pila tiene los siguientes elementos:")
        return [ print(i) for i in reversed(self._data) ]


def balanceador(expresion):
    stack = Stack()
    limiters = {')':'(', '}':'{', ']':'['}

    for character in expresion:
        if character in '([{':
            stack.push(character)
        elif character in ')]}':
            if stack.is_empty() or stack.top() != limiters[character]:
                return False
            stack.pop()
    return stack.is_empty()


expresion = "{(a + b) * [c + d]}" # TRUE
expresion1 = "{(a + b * [c + d]" # FALSE


if balanceador(expresion1):
    print('Los limitadores estan balanceados')
else:
    print('Los limitadores no estan balanceados')

#Instancia de Pila
pilaAAA = Stack()
pilaAAA.push(10)
pilaAAA.push(6)
pilaAAA.push(7)

pilaAAA.display()

print(pilaAAA.pop())



