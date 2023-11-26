# find the most frequent element in a linked_list
my_list = [1, 2, 2, 2, 3, 4, 3, 1]

most_frequent = max(set(my_list), key=my_list.count)

print(f"Most frequent element: {most_frequent}")
