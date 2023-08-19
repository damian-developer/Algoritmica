class queue:
    def __init__(self, capacity = 10):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._capacity = capacity

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError('La cola esta vacia')
        return self._data[self._front]

    def enqueue(self, item):
        if self._size == self._capacity:
            self._resize( 2 * self._capacity)
        back = (self._front + self._size) % self._capacity
        self._data[back] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('La cola esta vacia')
        element = self._data[self._front]
        self._data[self._front] = None 
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return element

    def _resize(self, capacity):
        new_data = [None] * capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % self._capacity]
        self._data = new_data
        self._front = 0
        self._capacity = capacity


cola = queue()
cola.enqueue(9)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(3)
cola.enqueue(3)

print(cola.first())
print(cola.dequeue())
print(cola.first())
print(len(cola))

while not cola.is_empty():
    print(cola.dequeue(), end=" ")

