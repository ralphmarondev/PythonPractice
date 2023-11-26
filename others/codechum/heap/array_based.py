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

	if largest != i:
		swap(arr, i, largest)
		heapify(arr, n, largest)

def buildHeap(arr, n):
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

def heapSort(arr):
	n = len(arr)
	buildHeap(arr, n)

	for i in range(n - 1, 0, -1):
		swap(arr, 0, i)
		heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)

print("Sorted array:", end=" ")
for num in arr:
	print(num, end=" ")
print()

