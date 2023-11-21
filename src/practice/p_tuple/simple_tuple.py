# reference: https://www.softwaretestinghelp.com/python/python-tuple/
def convert_list_to_tupple():
    my_list = [1, 2, 3, 4, 5]

    print(my_list)
    print(type(my_list))

    my_tuple = tuple(my_list)
    print(my_tuple)
    print(type(my_tuple))


def convert_tuple_to_string():
    my_tuple = ('r', 'a', 'l', 'p', 'h')
    my_str = "".join(my_tuple)

    print(my_str)


def packing_and_unpacking_tuple():
    my_tuple = ('Ralph', 2121800, 'Computer Engineer')
    (e_name, e_id, e_title) = my_tuple

    print(f"Packed tuple is: {my_tuple}")
    print(f"Name: {e_name}")
    print(f"Id: {e_id}")
    print(f"Title: {e_title}")


def named_tuple():
    # named tuple can be:
    # accessed by index, key, getattr() method
    import collections

    Employee = collections.namedtuple("Employee", ["Name", "Id", "Title"])
    Emp = Employee('Ralph', '21-21800', 'Computer Engineer')

    # accessing using index
    print(f"Employee name: {Emp[0]}")

    # accessing using key
    print(f"Employee ID: {Emp.Id}")

    # accessing gy getattr() method
    print(f"Employee title: {getattr(Emp, 'Title')}")


def named_tuple2():
    import collections

    Employee = collections.namedtuple('Employee', ['Name', 'Id', 'Title'])
    Emp = Employee('Ralph', '21-21800', 'Computer Engineer')
    Emp1 = ['Cazmir', '21-24345', 'Law']
    Emp2 = {'Name': 'Hana', 'Id': '21-21451', 'Title': 'Law'}

    # using _make()
    print(Employee._make(Emp1))

    # using _asdict()
    print(Emp._asdict())

    # using ** operator
    print(Employee(**Emp2))


# return tuple
def my_fun():
    name = 'Ralph'
    id = 2121800
    title = 'Computer Engineer'

    return (name, id, title)


def return_tuple():
    employee = my_fun()

    print(f'Employee details is: {employee}')


def deleting_tuple():
    # we cannot delete individual elements from tuple as tuple are immutable.
    # the only way to delete the elements from tuple is to delete the entire tuple
    # 'del' in-built function to delete the entire tuple
    my_tuple = (2, 4, 5, 'Python')

    print(f'Before deleting the tuple: {my_tuple}')
    del tuple
    print(f'After deleting the tuple: {my_tuple}')


def basic_tuple_operations():
    my_tuple1 = (3, 4, 'Ralph')
    my_tuple2 = (5, 6, 'Cazmir')

    print(f'Concatenation: {my_tuple1 + my_tuple2}')
    print(f'Tuple repetition: {my_tuple1 * 3}')
    print(f'Membership operation: {2 in my_tuple1}')


def built_in_tuple_methods():
    # any() -> returns True if any element present in a tuple
    #       and returns False if the tuple is empty
    my_tuple = (2, 4, 5)
    print(f'Any element present in my_tuple: {any(my_tuple)}')

    # min() -> returns smallest element(Integer) of the tuple
    print(f'Smallest element: {min(my_tuple)}')

    # max() -> returns largest element(Integer) of the tuple
    print(f'Largest element: {max(my_tuple)}')

    # len() -> returns the length of the tuple
    print(f'Length of tuple: {len(my_tuple)}')

    # sorted() -> used to sort all the elements of the tuple
    print(f'Sorted integer: {sorted(my_tuple)}')
    my_tuple2 = ('a', 'e', 'i', 'u', 'o')
    print(f'Sorted character: {sorted(my_tuple2)}')

    # sum() -> returns sum of all elements (Integers) of the tuple
    print(f'Sum of tuple: {sum(my_tuple)}')


if __name__ == '__main__':
    my_tuple = (3, 6, 5, 4)
    #
    # print(my_tuple.index(3)) # getting index of '3'
    # print(my_tuple.count(3)) # count '3' on tuple
    # print(my_tuple[0])       # accessing 1st element
    # print(my_tuple[-1])      # accessing last element

    # convert_list_to_tupple()
    # convert_tuple_to_string()

    # print(sorted(my_tuple))  # sorting tuple

    # packing_and_unpacking_tuple()
    # named_tuple()
    # named_tuple2()

    # return_tuple()
    # deleting_tuple()
    # basic_tuple_operations()
    built_in_tuple_methods()
