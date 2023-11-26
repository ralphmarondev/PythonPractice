# linked linked_list based stack implementation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return -1
        element = self.top.data
        self.top = self.top.next
        return element

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        return self.top.data


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
