# frequency of numbers in string
string = "ralphmaron1234"
freq = 0

for i in string:
    if i.isdigit():
        freq += 1

print(f"Frequency of numbers: {freq}")
