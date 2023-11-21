# check if a given string is binary string or not
def is_binary(string):

    for i in string:
        if i not in ("0","1"):
            return False
    return True


string = "ralph maron eda is cute"
# string = "100100010010" # True
print(is_binary(string))
