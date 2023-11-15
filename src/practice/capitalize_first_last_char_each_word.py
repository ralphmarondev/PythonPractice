# capitalize first and last char of each word in string
string = "ralph maron eda is cute"
string_list = string.split()
res = []
for i in string_list:
    x = i[0].upper() + i[1:-1]+i[-1].upper()
    res.append(x)

res = " ".join(res)
print(f"New String: {res}")



