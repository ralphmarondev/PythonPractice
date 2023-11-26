class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current.next:
            print(current.data, end=" ")
            current = current.next

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_pos(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(pos - 1):
            if current is None:
                print("Out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node


if __name__ == '__main__':
    link = LinkedList()

    link.insert_first(1)
    link.insert_first(0)
    link.insert_first(10)

    link.display()
