# swap commas and dots in a string
def approach_one(string):
    new_string = ""

    for i in string:
        if i == ".":
            new_string += ","
        elif i == ",":
            new_string += "."
        else:
            new_string += i


# using maketrans and translate
def approach_two(string):
    maketrans = string.maketrans
    final = string.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ',')


string = "ralph.maron,is,cute"

# print(approach_one(string))
print(approach_two(string))
