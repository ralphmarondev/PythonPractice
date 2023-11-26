# Function to find the length of the longest common subsequence of
# sequences `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y, m, n):
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0

    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        return LCSLength(X, Y, m - 1, n - 1) + 1

    # otherwise, if the last character of `X` and `Y` don't match
    return max(
        LCSLength(X, Y, m, n - 1),
        LCSLength(X, Y, m - 1, n))


def LSCLenght3(X, Y, Z, m, n, o, lookup):
    # end of sequence is reached
    if m == 0 or n == 0 or n == 0:
        return 0

    # unique key from dynamic element
    key = (m, n, o)

    # if subproblem is seen for the first time, solve it,
    # and store its result in a dictionary
    if key not in lookup:
        # last char matches
        if X[m - 1] == Y[n - 1] and Y[n - 1] == Z[o - 1]:
            lookup[key] = LSCLenght3(X, Y, Z, m - 1, n - 1, o - 1, lookup) + 1
        # if last char doesn't matches
        else:
            lookup[key] = max(
                LSCLenght3(X, Y, Z, m - 1, n, o, lookup),
                LSCLenght3(X, Y, Z, m, n - 1, o, lookup),
                LSCLenght3(X, Y, Z, m, n, o - 1, lookup)
            )
    return lookup[key]


# Function to find the length of the longest common subsequence of
# sequences X[0…m-1], Y[0…n-1], and Z[0…o-1]
def LCSLength3F(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)

    # T[m+1][n+1][o+1]: lookup table to store solution to already computed
    # subproblems, i.e., T[i][j][k] stores the length of LCS of substring
    # X[0…i-1], Y[0…j-1] and Z[0…k-1]

    T = [[[0 for k in range(o + 1)] for j in range(n + 1)] for i in range(m + 1)]

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                # if the current character of `X`, `Y`, and `Z` matches
                if X[i - 1] == Y[j - 1] and Y[j - 1] == Z[k - 1]:
                    T[i][j][k] = T[i - 1][j - 1][k - 1] + 1
                # otherwise, if the current character of `X`, `Y`, and `Z`
                # doesn't match
                else:
                    T[i][j][k] = max(T[i - 1][j][k], T[i][j - 1][k], T[i][j][k - 1])

    # LCS will be the last entry in the lookup table
    return T[m][n][o]




if __name__ == '__main__':
    X = 'ABCBDAB'
    Y = 'BDCABA'
    Z = 'BADACB'

    # dictionary to store solutions of subproblems

    print(f"The length of the LCS is: {LCSLength3F(X, Y, Z)}")
