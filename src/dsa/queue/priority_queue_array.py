# priority queue using array
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def enqueue(self, data, priority):
        new_element = (data, priority)
        self.elements.append(new_element)
        self.elements.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.elements:
            print("Priority queue is empty")
            return None
        return self.elements.pop(0)[0]

if __name__ == '__main__':
    queue = PriorityQueue()

    queue.enqueue(10, 2)
    queue.enqueue(20, 1)
    queue.enqueue(30,3)

    for i in range(3):
        print(f"Dequeued element: {queue.dequeue()}")

