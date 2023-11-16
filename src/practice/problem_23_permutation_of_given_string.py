# permutation of a given string

from itertools import permutations
# using built-in function
def using_built_in_function(string):
    perm_list = permutations(string)

    for perm in list(perm_list):
        print("".join(perm))


# string = "ABCD"
# using_built_in_function(string)


# using recursion
def using_recursion(string):
    if len(string) == 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]

        for perm in using_recursion(remaining_chars):
            permutations.append(fixed_char + perm)
    return permutations


string = "ralphmaron"
permutations_list =  using_recursion(string)
z = set(permutations_list)

for perm in z:
    print(perm)
