# set -> unordered collection of data types that is iterable
#       mutable and has no duplicate elements

def creating_set():
    my_set = set()
    print(f"Initial blank set: {my_set}")


def creating_set_with_use_of_string():
    my_set = set("RalphMaronCute")

    print(f"Set with use of string: {my_set}")


def creating_set_with_use_of_constructor():
    # using object to store string
    my_string = 'RalphMaronCute'
    my_set = set(my_string)

    print(f"Set with the use of an object: {my_set}")


def creating_set_with_use_of_list():
    my_set = set(['Ralph', 'Maron', 'is', 'cute'])

    print(f"Set with use of list: {my_set}")


def creating_set_with_use_of_tuple():
    my_tuple = ('Ralph', 'Maron', 'is', 'cute')
    my_set = set(my_tuple)

    print(f"Set with use of tuple: {my_set}")


def creating_set_with_use_of_dictionary():
    my_dictionary = {'Ralph': 1, 'Maron': 2, 'is': 3, 'cute': 4}
    my_set = set(my_dictionary)

    print(f"Set with use of dictionary: {my_set}")


def creating_set_with_another_method():
    my_set = {1, 2, 3, 3}  # no duplicates

    print(my_set)


def adding_element_in_set():
    my_set = {1, 2, 3}

    for i in range(1, 6):
        my_set.add(i)

    print(f"Set after addition of element: {my_set}")


def updating_element_in_set():
    my_set = {1, 5, 2, 3}

    my_set.update([10, 11])
    print(f"Set after addition of element using update: {my_set}")


class ImplementingAllFunctions:
    def create_set(self):
        my_set = {1, 2, 3, 4, 5}
        print(f"Create set: {my_set}")

    def add_element(self):
        my_set = {1, 2, 3, 4, 5}
        my_set.add(6)
        print(f"Add element: {my_set}")

    def remove_element(self):
        my_set = {1, 2, 3, 4, 5}
        my_set.remove(3)
        print(f"Remove element: {my_set}")

    def clear_set(self):
        my_set = {1, 2, 3, 4, 5}
        my_set.clear()
        print(f"Clear set: {my_set}")

    def set_union(self):
        my_set1 = {1, 2, 3}
        my_set2 = {4, 5, 6}

        my_set = my_set1.union(my_set2)
        print(f"Set union: {my_set}")

    def set_intersection(self):
        my_set1 = {1, 2, 3, 4, 5}
        my_set2 = {4, 5, 6, 7, 8}

        my_set = my_set1.intersection(my_set2)
        print(f"Set interaction: {my_set}")

    def set_difference(self):
        my_set1 = {1, 2, 3, 4, 5}
        my_set2 = {4, 5, 6, 7, 8}

        my_set = my_set1.difference(my_set2)
        print(f"Set difference: {my_set}")

    def set_symmetric_difference(self):
        my_set1 = {1, 2, 3, 4, 5}
        my_set2 = {4, 5, 6, 7, 8}

        my_set = my_set1.symmetric_difference(my_set2)
        print(f"Set symmetric difference: {my_set}")

    def set_subset(self):
        my_set1 = {1, 2, 3, 4, 5}
        my_set2 = {2, 3, 4}

        subset = my_set2.issubset(my_set2)
        print(f"Set subset: {subset}")

    def set_superset(self):
        my_set1 = {1, 2, 3, 4, 5}
        my_set2 = {2, 3, 4}

        superset = my_set2.issubset(my_set2)
        print(f"Set superset: {superset}")


if __name__ == '__main__':
    # creating_set()
    # creating_set_with_use_of_string()
    # creating_set_with_use_of_constructor()
    # creating_set_with_use_of_list()
    # creating_set_with_use_of_tuple()
    # creating_set_with_use_of_dictionary()
    # creating_set_with_another_method()
    # adding_element_in_set()
    # updating_element_in_set()

    implement = ImplementingAllFunctions()

    implement.create_set()
    implement.add_element()
    implement.remove_element()
    implement.clear_set()
    implement.set_union()
    implement.set_intersection()
    implement.set_difference()
    implement.set_symmetric_difference()
    implement.set_subset()
    implement.set_superset()

    print()
