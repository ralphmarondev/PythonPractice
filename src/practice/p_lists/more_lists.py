my_list = [10, 50, 20, 30, 40]
def join_list():
    # python join list
    my_foods = ['pizza', 'falafel', 'carrot cake']
    my_foods_csv = ",".join(my_foods)
    print(my_foods_csv)

def sum_list():
    # _sum = sum(my_list)
    my_str_nums = "10,50,20,40,30"
    my_str_list = my_str_nums.split(",")
    _sum = sum([int(i) for i in my_str_list if i.isnumeric()])

    print(_sum)


if __name__ == '__main__':
    print()
    # remove duplicates
    my_list = [1, 4, 2, 1, 1]
    my_unique_list = []

    for i in my_list:
        if i not in my_unique_list:
            my_unique_list.append(i)

    print(my_unique_list)
