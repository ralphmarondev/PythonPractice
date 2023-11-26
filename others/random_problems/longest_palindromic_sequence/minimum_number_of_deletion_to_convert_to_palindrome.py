# Function to find out the minimum number of deletions required to
# convert a given string `X[i…j]` into a palindrome
def minDeletions(X, i, j, lookup):
    # base condition
    if i >= j:
        return 0

    # construct a unique key from dynamic elements of the input
    key = (i, j)

    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        # if the last character of the string is the same as the first character
        if X[i] == X[j]:
            lookup[key] = minDeletions(X, i + 1, j - 1, lookup)
        else:
            # if the last character of the string is different from the first character

            # 1. Remove the last character and recur for the remaining substring
            # 2. Remove the first character and recur for the remaining substring

            # return 1 (for remove operation) + minimum of the two values

            result = 1 + min(minDeletions(X, i, j - 1, lookup),
                             minDeletions(X, i + 1, j, lookup))
            lookup[key] = result

    # return the subproblem solution from the dictionary
    return lookup[key]

# if __name__ == '__main__':
#     X = 'ACBCDBAA'
#     n = len(X)
#
#     # create a dictionary to store solutions to subproblems
#     lookup = {}
#
#     print('The minimum number of deletions required is',
#           minDeletions(X, 0, n - 1, lookup))


# USING LCS
# Function to find out the minimum number of deletions required to
# convert a given string `X[0…n-1]` into a palindrome
def minDeletions(X):
    n = len(X)

    # string 'Y' is a reverse of 'X'
    Y = X[::-1]

    # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(n + 1)] for y in range((n + 1))]

    # fill the lookup table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # if current character of 'X' and 'Y' matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1

            # otherwise, if the current character of 'X' and 'Y' don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

    # Now, `lookup[n][n]` contains the size of the longest palindromic subsequence.

    # The minimum number of deletions required will be the difference in the size
    # of the string and the size of the palindromic subsequence

    return n - lookup[n][n]


if __name__ == '__main__':
    X = 'ACBCDBAA'

    print('The minimum number of deletions required is', minDeletions(X))

