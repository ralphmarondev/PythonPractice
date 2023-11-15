# check if string contains a special character
string = "ralphmaron*"

for i in string:
    if not i.isdigit() or not i.isalpha():
        print("Contains special char")

print("Does not contain special chars")
# https://www.geeksforgeeks.org/python-string-exercise/
