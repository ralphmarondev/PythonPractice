# Function to find the length of the longest repeated subsequence
# of substring `X[0…m-1]` and `X[0…n-1]`
def LRSLength(X, m, n, lookup):
    # return if the end of either string is reached
    if m == 0 or n == 0:
        return 0

    # construct a unique key from dynamic elements of the input
    key = (m, n)

    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        # if characters at index `m` and `n` matches and the index are different
        if X[m - 1] == X[n - 1] and m != n:
            lookup[key] = LRSLength(X, m - 1, n - 1, lookup) + 1
        else:
            # otherwise, if characters at index `m` and `n` don't match
            lookup[key] = max(LRSLength(X, m, n - 1, lookup),
                              LRSLength(X, m - 1, n, lookup))

    # return the subproblem solution from the dictionary
    return lookup[key]


if __name__ == '__main__':
    X = 'ATACTCGGA'
    m = len(X)

    # create a dictionary to store solutions to subproblems
    lookup = {}

    print('The length of the longest repeating subsequence is',
          LRSLength(X, m, m, lookup))
