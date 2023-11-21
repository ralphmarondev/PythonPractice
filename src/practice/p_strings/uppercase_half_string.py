# uppercase half string
string = "ralphmaron"
mid_index = len(string) // 2

new_string = string[mid_index:]
new_string = new_string.upper()
print(string[:mid_index] + new_string)
