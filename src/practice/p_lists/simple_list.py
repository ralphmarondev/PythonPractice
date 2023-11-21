def filtering_list(my_list: list[int]):
    # my_filtered_list = list(filter(lambda x: x > 20, my_list))
    my_filtered_list = [item for item in my_list if item > 20]

    return my_filtered_list


def modifying_list(my_list: list[int]):
    modified_list = list(map(lambda x: (x * x) if x > 10 else x, my_list))

    return modified_list


def combining_list(my_list:list[int]):
    my_second_list = [60, 80,70]

    my_combined_list = list(zip(my_list, my_second_list))

    return my_combined_list


def most_common_item(my_list: list[int]):
    most_frequent_value = max(set(my_list), key=my_list.count)

    return most_frequent_value


def flatten_list_of_lists(my_list_of_lists: list[list[int]]):

    my_flattened_list = [item for List in my_list_of_lists for item in List]

    return my_flattened_list


if __name__ == '__main__':
    my_list = [10, 20, 50, 30, 10, 20]
    my_list_of_lists = [
        [10, 20],
        [50, 30],
        [10, 20]
    ]

    print(my_list)

    # print(flatten_list_of_lists(my_list_of_lists))
