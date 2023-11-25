# largest common substring
def largest_common_substring(x, y, m, n):
    max_length = 0  # max length of lcs
    ending_index = m  # ending index of lcs in 'x'

    # lookup [i][j] stores the length of lcs of 'x[0..-1]' and 'y[0..j-1]
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current char of 'x' and 'y' matches
            if x[i - 1] == y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                print(f"Lookup[{i}][{j}]: {lookup[i][j]}")
                # update the maximum length and ending index
                if lookup[i][j] > max_length:
                    max_length = lookup[i][j]
                    ending_index = i
                    print(f"max_length: {max_length}, ending_index: {ending_index}")

    # return longest common substring having length 'max_length'
    return x[ending_index - max_length: ending_index]


if __name__ == '__main__':
    x = 'ABC'
    y = 'BABA'
    m = len(x)
    n = len(y)
    print(largest_common_substring(x, y, m, n))
