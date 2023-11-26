class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_pos(self, data, pos=0):
        new_node = Node(data)
        current = self.head

        if pos == 0:
            self.insert_first(new_node)
            return

        for i in range(pos - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head

        if current:
            while current:
                print(current.data, end=' ')
                current = current.next
        else:
            print("List is empty")

    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List is empty. Nothing to delete.")

    def delete_last(self):
        current = self.head

        if not self.head:
            print("List is empty")
            return

        if not self.head.next:
            self.head = None
        return

        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_pos(self, pos):
        current = self.head

        if not self.head:
            print("List is empty")
            return

        if pos == 0:
            self.head = self.head.next
            return

        for i in range(pos - 1):
            if current is None or current.next is None:
                print("Position out of bounds.")
                return
            current = current.next
        current.next = current.next.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.display()
    ll.insert_first(20)
    ll.insert_first(10)
    ll.insert_last(30)
    ll.display()

    print()
    ll.insert_at_pos(15, 2)
    ll.insert_at_pos(5, 2)
    ll.display()

    print()
    ll.delete_at_pos(2)
    ll.display()
