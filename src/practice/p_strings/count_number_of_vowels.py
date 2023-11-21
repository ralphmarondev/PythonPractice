# count number of vowels in a string
string = "ralphmaron"

vowels = set("aeiou")
vowels_present = []

for i in string:
    if i in vowels:
        vowels_present.append(i)

print(len(vowels_present))
