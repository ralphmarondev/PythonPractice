class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, element):
        new_node = Node(element)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue underflow")
            return -1
        element = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return element

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return -1
        return self.front.data

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Peek: {queue.peek()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Peak: {queue.peek()}")
