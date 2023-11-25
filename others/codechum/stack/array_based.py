# array based stack implementation
MAX_SIZE = 100


class Stack:
    def __init__(self):
        self.data = [None] * MAX_SIZE
        self.top = -1

    def push(self, element):
        if self.top == MAX_SIZE - 1:
            print("Stack overflow")
            return
        self.top += 1
        self.data[self.top] = element

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return -1  # return a sentinel value indicating error

        element = self.data[self.top]
        self.top -= 1
        return element

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return -1
        return self.data[self.top]


def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")


if __name__ == '__main__':
    main()
   