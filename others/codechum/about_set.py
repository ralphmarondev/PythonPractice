my_set = {1, 2, 3}
print(my_set)

my_set.add(4)
print(my_set)

my_set.update([3,4,5])
print(my_set)

# my_set.remove(0)  # gives error if not present
my_set.discard(0)   # don't give error
last = my_set.pop() # removes and return an arbitrary element
print(last)
print(my_set)