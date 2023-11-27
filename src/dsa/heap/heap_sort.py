# heapsort
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if i != largest:
        swap(arr, i, largest)
        heapify(arr, n, largest)


def build_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)

    for i in range(n - 1, 0, -1):
        swap(arr, 0,i)
        heapify(arr, i, 0)

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))

        arr.append(element)
    print("Original array: ", arr)
    print()
    heap_sort(arr)

    print("Sorted elements:", end=' ')
    for num in arr:
        print(num, end=' ')
    print()
