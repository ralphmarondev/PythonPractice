class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        return None if self.is_empty() else self.top.data

    def reverse(self):
        prev = None
        current = self.top
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev

    def search(self, target):
        index = 0
        current = self.top
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.peek())  # Output: 3

print("Pop:", stack.pop())  # Output: 3

print("Stack after pop:", stack.peek())  # Output: 2

stack.reverse()
print("Stack after reverse:", stack.peek())  # Output: 1

print("Search for 2:", stack.search(2))  # Output: -1 (not found)
print("Search for 1:", stack.search(1))  # Output: 1 (found at index 1)
