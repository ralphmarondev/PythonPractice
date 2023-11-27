class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]
        return None

    def __str__(self):
        return str(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
        self.front = None

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def __str__(self):
        return str(self.queue)

if __name__ == '__main__':
    # region Stack
    # stack = Stack()
    #
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    #
    # print(stack.__str__())
    #
    # stack.pop()
    # print(stack.__str__())
    # endregion Stack
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.__str__())

    queue.dequeue()
    print(queue.__str__())
