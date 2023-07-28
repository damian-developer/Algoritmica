class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # si la cabecera es NONE
            self.head = new_node
            return

        current = self.head # el valor actual de la cabecera
        while current.next: #recorre hasta el ultimo elemento, si es NONE se detiene y sale
            current = current.next

        current.next = new_node
    
    def remove_first(self):
        if not self.head:
            print("La lista está vacía. No se puede eliminar.")
            return

        self.head = self.head.next    

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


my_list = LinkedList()
my_list.insert_at_beginning(1)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(4)

my_list.insert_at_end(1)
my_list.insert_at_end(5)

my_list.remove_first()
my_list.display()

