# odd frequency character
string = "ralph maron eda is cute"

temp_str = set(string)
result = []

for i in temp_str:
    if string.count(i) % 2 != 0:
        result.append(i)

print(str(result))
