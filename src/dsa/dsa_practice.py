class MaxHeap:
    def __init__(self):
        self.heap = []

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        if self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = 2 * index
        right = 2 * index + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if index != largest:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubble_down(1)
            return max
        if len(self.heap) == 2:
            max = self.heap.pop()
            return max
        return None

if __name__ == '__main__':
    m = MaxHeap()

    m.push(3)
    m.push(1)
    m.push(4)
    m.push(1)
    m.push(5)
    print(m.heap)

    print(m.pop())
    print(m.heap)
