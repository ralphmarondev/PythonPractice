class Queue:
    def __init__(self):
        self.data = []
        self.front = 0
        self.rear = -1

    def enqueue(self, element):
        self.data.append(element)
        self.rear += 1

    def dequeue(self):
        if self.front > self.rear:
            print("Queue underflow")
            return -1
        element = self.data[self.front]
        self.front += 1
        return element

    def peek(self):
        if self.front > self.rear:
            print("Queue is empty")
            return -1
        return self.data[self.front]


if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Peek: {queue.peek()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Peek: {queue.peek()}")
