def accepting_user_input_using_loop():
    n = int(input("Enter size of list: "))
    my_list = []

    for i in range(n):
        my_list.append(int(input()))

    print(my_list)


def accepting_user_input_using_map():
    n = int(input("Enter size of list: "))

    my_list = list(map(int, input("Enter integer element: ").strip().split()))[:n]

    print(my_list)


def get_list_of_input():
    my_list = []
    n = int(input("Enter size of list: "))

    for i in range(n):
        element = [input(), int(input())]
        my_list.append(element)

    print(my_list)


def get_using_list_comprehension_and_typecasting():
    my_int_list = []
    my_char_list = []

    my_int_list = [int(item) for item in input("Enter list item: ").split()]
    my_char_list = [char for char in input("Enter list items: ").split()]

    print(my_int_list)
    print(my_char_list)


if __name__ == '__main__':
    # accepting_user_input_using_loop()
    # accepting_user_input_using_map()
    # get_list_of_input()
    get_using_list_comprehension_and_typecasting()

    print()
