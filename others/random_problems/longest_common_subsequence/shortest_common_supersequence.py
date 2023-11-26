# Function to return all SCS of substrings `X[0…m-1]`, `Y[0…n-1]`
def SCS(X, Y, m, n, lookup):
    # if the end of the first string is reached, create a linked_list
    # containing the second substring and return
    if m == 0:
        return {Y[:n]}

    # if the end of the second string is reached, create a linked_list
    # containing the first substring and return
    elif n == 0:
        return {X[:m]}

    # if the last character of `X` and `Y` is the same, it should occur
    # only one time in SSC
    if X[m - 1] == Y[n - 1]:
        # find all SCS of substring `X[0…m-2]` and `Y[0…n-2]`
        scs = SCS(X, Y, m - 1, n - 1, lookup)

        # append the current character `X[m-1]` or `Y[n-1]` to all SCS of
        # substring `X[0…m-2]` and `Y[0…n-2]`

        return {str + X[m - 1] for str in scs}

    # we reach here when the last character of `X` and `Y` don't match

    # if a top cell of the current cell has more value than the left cell,
    # then append the current character of string `X` to all SCS of
    # substring `X[0…m-2]`, `Y[0…n-1]`

    if lookup[m - 1][n] > lookup[m][n - 1]:
        scs = SCS(X, Y, m - 1, n, lookup)
        return {str + X[m - 1] for str in scs}

    # if a left cell of the current cell has more value than the top cell,
    # then append the current character of string `Y` to all SCS of
    # substring `X[0…m-1]`, `Y[0…n-2]`

    if lookup[m][n - 1] > lookup[m - 1][n]:
        scs = SCS(X, Y, m, n - 1, lookup)
        return {str + Y[n - 1] for str in scs}

    # if the top cell value is the same as the left cell, then go in both
    # top and left directions

    # append the current character of string `X` to all SCS of
    # substring `X[0…m-2]`, `Y[0…n-1]`
    top = SCS(X, Y, m - 1, n, lookup)

    # append the current character of string `Y` to all SCS of
    # substring `X[0…m-1]`, `Y[0…n-2]`
    left = SCS(X, Y, m, n - 1, lookup)

    return set([str + X[m - 1] for str in top] + [str + Y[n - 1] for str in left])


# Function to fill the lookup table by finding the length of LCS
# of substring `X[0…m-1]` and `Y[0…n-1]`
def LCS(X, Y, m, n, lookup):
    # Fill the lookup table in a bottom-up manner.
    # the first row and first column of the lookup table are already 0.
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


# Function to find all shortest common supersequence of string `X` and `Y`
def findSCS(X, Y):
    m = len(X)
    n = len(Y)

    # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # fill lookup table
    LCS(X, Y, m, n, lookup)

    # return all the longest common sequences
    return SCS(X, Y, m, n, lookup)


if __name__ == '__main__':
    X = 'ABCBDAB'
    Y = 'BDCABA'

    # Find all shortest common supersequence of string `X` and `Y`
    scs = findSCS(X, Y)

    # print all SCS present in the set
    print(f'All shortest common supersequence of {X} and {Y} are:', scs)
