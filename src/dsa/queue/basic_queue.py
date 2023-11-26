class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def sort(self):
        sorted_list = sorted(self._to_list())
        self._from_list(sorted_list)

    def search(self, item):
        return item in self._to_list()

    def reverse(self):
        items_list = self._to_list()
        items_list.reverse()
        self._from_list(items_list)

    def display(self):
        current = self.front

        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def _to_list(self):
        item_list = []
        current = self.front

        while current:
            item_list.append(current.data)
            current = current.next
        return item_list

    def _from_list(self, item_list):
        self.front = self.rear = None

        for item in item_list:
            self.enqueue(item)


if __name__ == '__main__':
    q = Queue()

    print(f"Is queue empty: {q.is_empty()}")

    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(1)

    print("Queue after enqueuing: ")
    q.display()

    print(f"Dequeue: {q.dequeue()}")
    print("Queue after dequeuing: ")
    q.display()

    print(f"Is 8 in the queue: {q.search(8)}")

    print("Queue before sorting:")
    q.display()

    q.sort()
    print("Queue after sorting:")
    q.display()

    print("Queue before reversing:")
    q.display()

    q.reverse()
    print("Queue after reversing:")
    q.display()
