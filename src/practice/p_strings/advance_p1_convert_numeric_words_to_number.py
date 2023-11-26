# convert numeric words to number

# using loop + join() + split()
def approach_one():
    help_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    # initializing string
    test_str = "zero four zero one fjjf"

    result = "".join(help_dict[ele] for ele in test_str.split())

    return result


# using word2number
# NOTE: this ain't working lol :<
from word2number import w2n


def approach_two():
    test_str = "zero four zero one"

    result = w2n.word_to_num(test_str)
    return result


# using dictionary
def approach_three():
    words_to_digit = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    test_str = "zero one four two"

    words = test_str.split()
    digits = [words_to_digit[word] for word in words]

    result = "".join(digits)
    return result


# using linked_list of tuples
def approach_four():
    word_digit_pairs = [
        ('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9')
    ]

    test_str = "zero four zero one"

    for word, digit in word_digit_pairs:
        test_str = test_str.replace(word,digit)

    return test_str


print(approach_four())
