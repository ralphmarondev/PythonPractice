class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


if __name__ == '__main__':
    # create a doubly linked list: 1 <=> 2 <=> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    # traverse and print the elements of the linked list
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
