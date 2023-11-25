class ListFunctions:
    def simple_list(self):
        numbers = [1, 2, 3, 4, 2]
        # numbers.remove(2)
        for i in numbers:
            numbers.remove(2)

        print(numbers)


class ListComprehension:
    def simple_comprehension(self):
        list1 = [1, 2, 3]
        list2 = [10, 20]
        list3 = [10]

        pairs = [(x, y, z) for x in list1 for y in list2 for z in list3]
        print(pairs)


if __name__ == '__main__':
    demo = ListComprehension()

    demo.simple_comprehension()

