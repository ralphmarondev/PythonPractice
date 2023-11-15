# remove all duplicates from a given string
string = "ralphmaron"
my_list = []

for i in string:
    if i not in my_list:
        my_list.append(i)

for i in my_list:
    print(i, end="")
