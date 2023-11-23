# list comprehension syntax
# new_list = [expression(element) for element in old_list if condition]

def square_numbers():
    numbers = [1, 2, 3, 4, 5]

    squared = [x ** 2 for x in numbers]
    print(squared)


def iteration_with_list_comprehension():
    my_list = [item for item in [1, 2, 3]]

    print(my_list)


def even_list():
    my_list = [item for item in range(11) if item % 2 == 0]

    print(my_list)


def matrix_using_list_comprehension():
    matrix = [[j for j in range(3)] for i in range(3)]

    print(matrix)


def transpose_of_2d_matrix():
    two_d_matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    # generate transpose
    trans = [[i[j] for i in two_d_matrix] for j in range(len(two_d_matrix[0]))]
    print(trans)


def toggle_each_char_in_string():
    my_string = "RalphMaronIsCute"

    # toggle case of each char
    my_list = list(map(lambda i: chr(ord(i) ^ 32), my_string))
    print(my_list)


def create_list_of_tuples_from_two_separate_list():
    names = ['Ralph', 'Cazmir', 'Hana']
    ages = [20, 21, 21]

    person_tuples = [(name, age) for name, age in zip(names, ages)]
    print(person_tuples)


def reverse_each_string_in_list():
    my_list = [string[::-1] for string in ['Ralph', 'Maron', 'is', 'cute']]

    print(my_list)


# create a list and find the digit sum of every odd element in list
def digit_sum(digit):
    d_sum = 0
    for i in str(digit):
        d_sum += int(i)
    return d_sum


def display_sum_of_digits_of_all_odd_element():
    my_list = [367, 111, 562, 945, 6726, 873]

    new_list = [digit_sum(i) for i in my_list if i % 2 != 0]
    print(new_list)


if __name__ == '__main__':
    # square_numbers()
    # iteration_with_list_comprehension()
    # even_list()
    # matrix_using_list_comprehension()
    # transpose_of_2d_matrix()
    # toggle_each_char_in_string()
    # reverse_each_string_in_list()
    # create_list_of_tuples_from_two_separate_list()
    display_sum_of_digits_of_all_odd_element()
    print()
