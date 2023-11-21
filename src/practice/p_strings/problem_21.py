# program to find uncommon words from two strings
def get_uncommon_words(string1, string2):
    uncommon_words = []
    for i in string1:
        if i not in string2:
            uncommon_words.append(i)
    return uncommon_words


string1 = "ralph maron eda"
string2 = "ralph maron eda is cute"

string1_list = string1.split(" ")
string2_list = string2.split(" ")

uncommon_words = []

if len(string2_list) > len(string1_list):
    uncommon_words = get_uncommon_words(string2_list, string1_list)
else:
    uncommon_words = get_uncommon_words(string1_list, string2_list)

print(uncommon_words)
