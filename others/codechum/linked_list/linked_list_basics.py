class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds.")
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List is empty. Nothing to delete.")

    def delete_last(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(position - 1):
            if current is None or current.next is None:
                print("Position out of bounds.")
                return
            current = current.next

        current.next = current.next.next

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

if __name__ == "__main__":
    linked_list = LinkedList()

    # Insert at the beginning
    linked_list.insert_at_beginning(1)

    # Insert at specific positions
    linked_list.insert_at_position(2, 1)
    linked_list.insert_at_position(3, 2)

    # Insert at the end
    linked_list.insert_at_end(4)

    # Display the linked list
    print("Linked List:")
    linked_list.display()

    # Delete operations
    linked_list.delete_first()
    linked_list.delete_last()
    linked_list.delete_at_position(1)

    # Display the modified linked list
    print("\nModified Linked List:")
    linked_list.display()

    # Reverse the linked list
    linked_list.reverse()
    print("\nReversed Linked List:")
    linked_list.display()
