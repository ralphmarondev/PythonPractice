# find all close matches of input string from a linked_list
import difflib

def get_close_matches(string,pattern):
    return difflib.get_close_matches(string, pattern)


pattern = ['ape','apple','peach','puppy']
string = "appel"

print(get_close_matches(string, pattern))
