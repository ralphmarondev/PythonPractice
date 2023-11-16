# check for url in a string
def find(string):
    string_list = string.split()
    result = []

    for i in string_list:
        if i.startswith("https:") or i.startswith("http:"):
            result.append(i)
    return result

string = "My Profile: https://com.maronworks.com/ralphmaron/my-python-programs hosted by http://www.github.com"

print(f"Urls: {find(string)}")
