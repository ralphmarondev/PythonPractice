# singly linked linked_list in python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def get_count(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
        return count

    def search(self, element):
        current = self.head

        while current:
            if current.data == element:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_n = current.next
            current.next = prev
            prev = current
            current = next_n
        self.head = prev

    def sort_list(self):
        if self.head is None or self.head.next is None:
            return

        sorted_end = None
        while sorted_end != self.head.next:
            current = self.head

            while current.next != sorted_end:
                if current.data > current.next.data:
                    # swap data if the current node is greater than
                    # the next node
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            sorted_end = current

    def display(self):
        if self.is_empty():
            print("List is empty!")
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
            print()

    def insert_first(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        if self.is_empty():
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_pos(self, data, pos):
        new_node = Node(data)

        if self.is_empty() or pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(pos):
            if not current:
                print("Index out of bound")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node


if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_last(5)
    ll.display()

    ll.insert_last(10)
    ll.display()
    print(f"count: {ll.get_count()}")

    ll.insert_first(2)
    ll.display()

    ll.insert_at_pos(3, 1)
    ll.display()
    print(f"count: {ll.get_count()}")

    ll.reverse()
    ll.display()

    ll.sort_list()
    print(f"Sorted linked_list:")
    ll.display()
