# find words which are greater than given lenght k
input_string = "hello there, ralph maron eda is cute!!!"
k = 4

string_list = input_string.split()
final_list = []

for i in string_list:
    if len(i) > k:
        final_list.append(i)

for i in final_list:
    print(i, end=" ")
