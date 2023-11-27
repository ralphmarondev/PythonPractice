class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return None

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.__str__())
    print(f"Popped data: {stack.pop()}")
    print(stack.__str__())
