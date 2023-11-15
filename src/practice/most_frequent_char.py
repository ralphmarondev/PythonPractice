# most frequent char in string
string = "aabbbcdd"

all_freq = {}
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

res = max(all_freq, key=all_freq.get)
print(str(res))


