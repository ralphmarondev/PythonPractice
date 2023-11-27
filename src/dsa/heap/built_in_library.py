def min_heap():
    import heapq

    # creating min-heap
    min_heap = [3, 1, 4, 1, 5]
    heapq.heapify(min_heap)

    # pushing a new element
    heapq.heappush(min_heap, 2)

    # popping smallest element
    min_element = heapq.heappop(min_heap)

    print(min_element)
    print(min_heap)

def max_heap():
    import heapq

    # Creating a max-heap (using negation to simulate max-heap behavior)
    max_heap = [-3, -1, -4, -1, -5]
    heapq.heapify(max_heap)

    # Pushing a new element
    heapq.heappush(max_heap, -2)

    # Popping the largest element
    max_element = -heapq.heappop(max_heap)

    print(max_element)  # Output: 5
    print(max_heap)  # Output: [-1, -2, -4, -3]

if __name__ == '__main__':
    # max_heap()
    min_heap()
