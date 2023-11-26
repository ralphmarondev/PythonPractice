import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def enqueue(self, data, priority):
        new_element = (priority, data)
        heapq.heappush(self.elements, new_element)

    def dequeue(self):
        if not self.elements:
            print("Priority queue is empty")
            return None

        return heapq.heappop(self.elements)[1]


if __name__ == '__main__':
    queue = PriorityQueue()

    queue.enqueue(10, 2)
    queue.enqueue(20, 1)
    queue.enqueue(30, 3)

    for i in range(3):
        print(f"Dequeued element: {queue.dequeue()}")
