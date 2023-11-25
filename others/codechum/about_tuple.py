def tuple_basic():
    # tuple packing
    my_tuple = 1, 2, 3

    print(my_tuple)
    print(type(my_tuple))


class TupleBasicOperation:
    def concatenation(self):
        tuple1 = (1, 2, 3)
        tuple2 = ('a', 'b', 'c')
        concatenated_tuple = tuple1 + tuple2

        print(concatenated_tuple)

    def repetition(self):
        my_tuple = (1, 2)
        repeated_tuple = my_tuple * 3

        print(repeated_tuple)


if __name__ == '__main__':
    t = TupleBasicOperation()

    # t.concatenation()
    t.repetition()
