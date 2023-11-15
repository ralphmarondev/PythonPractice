# count the number of matching chars in a pair of string
string1 = "ralph"
string2 = "maron"

string1 = list(set(string1))
string2 = list(set(string2))
matched_chars = []

for i in string1:
    if i in string2:
        matched_chars.append(i)

print(len(matched_chars))
