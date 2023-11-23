def accepting_user_input_using_map():
    n = int(input("Enter size of list: "))

    lst = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]

    print(lst)


def map_demo():
    numbers = [1, 2, 3, 4, 5]
    result = map(lambda x: x * 2, numbers)
    print(numbers)
    print(list(result))


def add_two_list_using_map_and_lambda():
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]

    result = map(lambda x, y: x + y, numbers1, numbers2)
    print(list(result))


# double even numbers and leave odd numbers as is
def exercise1():
    numbers = [1, 2, 3, 4, 5]

    result = map(lambda x: x * 2 if x % 2 == 0 else x, numbers)
    print(list(result))


if __name__ == '__main__':
    exercise1()
