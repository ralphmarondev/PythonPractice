class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    # create a singly linked linked_list: 1 -> 2 -> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.next = third

    # traverse and print the elements of the linked linked_list
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
