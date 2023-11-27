# Max Heap
class MaxHeap:
    def __init__(self, items=[]):
        self.heap = []

        for i in items:
            self.heap.append(i)
            self.__float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return None

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

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        if self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.head) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == '__main__':
    m = MaxHeap([20, 30])

    m.push(10)
    print(str(m.heap))
