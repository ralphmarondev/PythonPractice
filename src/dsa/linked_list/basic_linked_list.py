# single linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        if not self.is_empty():
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
            print()
            return
        print("List is empty!")

    def insert_first(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data)
            return

        new_node = Node(data)
        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_pos(self, data, pos):
        if pos == 0 or self.is_empty():
            self.insert_first(data)
            return

        new_node = Node(data)
        current = self.head

        for i in range(pos - 1):
            if current.next is None:
                print("Out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_first(self):
        if self.is_empty():
            print("List is empty")
            return
        self.head = self.head.next

    def delete_last(self):
        if self.is_empty():
            print("List is empty")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_pos(self, pos):
        if self.is_empty():
            print("List is empty!")
            return

        if pos == 0:
            self.delete_first()
            return

        current = self.head
        for i in range(pos - 1):
            if current is None or current.next is None:
                print("Out of bound")
                return
            current = current.next
        current.next = current.next.next

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def search(self, data):
        current = self.head

        if self.is_empty():
            print("List is empty!")
            return

        m_list = []
        while current:
            m_list.append(current.data)
            current = current.next

        return data in m_list

    def merge_sort(self):
        self.head = self._merge_sort_linked_list(self.head)

    def _merge_sort_linked_list(self, head):
        if head is None or head.next is None:
            return head

        # Split the linked list into two halves
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Recursively sort both halves
        left = self._merge_sort_linked_list(head)
        right = self._merge_sort_linked_list(next_to_middle)

        # Merge the sorted halves
        sorted_list = self._merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return None

        slow_ptr = head
        fast_ptr = head.next

        while fast_ptr is not None:
            fast_ptr = fast_ptr.next
            if fast_ptr is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next

        return slow_ptr

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data < right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result


def input_data():
    data = input("Enter data: ")
    return data


def input_pos():
    pos = int(input("Enter position: "))
    return pos


def input_search():
    to_search = input("Enter element to search: ")
    return to_search


if __name__ == '__main__':
    ll = LinkedList()

    choices_list = [
        'Insert First', 'Insert Last', 'Insert at position',
        'Delete First', 'Delete Last', 'Delete at position',
        'Is empty', 'Reverse', 'Search', 'Sort'
    ]
    for index, item in enumerate(choices_list):
        print(f"{index + 1}-{item}")

    while True:
        try:
            choice = int(input("> "))
        except:
            print("Choice must me an integer!")

        if choice == 1:
            data = input_data()
            ll.insert_first(data)
        elif choice == 2:
            data = input_data()
            ll.insert_last(data)
        elif choice == 3:
            data = input_data()
            pos = input_pos()
            ll.insert_at_pos(data, pos)
        elif choice == 4:
            ll.delete_first()
        elif choice == 5:
            ll.delete_last()
        elif choice == 6:
            pos = input_pos()
            ll.delete_at_pos(pos)
        elif choice == 7:
            print(f"Is empty: {ll.is_empty()}")
        elif choice == 8:
            ll.reverse()
        elif choice == 9:
            to_search = input_search()
            print(f"Is present: {ll.search(to_search)}")
        elif choice == 10:
            ll.merge_sort()
        else:
            print("Error")
        print("Elements: ", end="")
        ll.display()
