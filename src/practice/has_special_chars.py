# check if string contains a special character
def has_special_string(string):
    for i in string:
        if not i.isdigit() or not i.isalpha() or i == " ":
            return True
    return False
    # https://www.geeksforgeeks.org/python-string-exercise/

string = "ralphmaron*"

if has_special_string(string):
    print("Contains special char")
else:
    print("Does not contain special chars")
