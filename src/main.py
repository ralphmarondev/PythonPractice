# largest common substring
def longest_common_substring(test_str1, test_str2):
    m = len(test_str1)
    n = len(test_str2)

    common_suffixes = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if test_str1[i - 1] == test_str2[j - 1]:
                common_suffixes[j][j] = common_suffixes[i - 1][j - 1] + 1
                if common_suffixes[i][j] > max_length:
                    max_length = common_suffixes[i][j]
                    end_index = i - 1
            else:
                common_suffixes[i][j] = 0

    longest_substring = test_str1[end_index - max_length + 1: end_index + 1]


if __name__ == '__main__':
    test_str1 = 'abcdef'
    test_str2 = 'zabcde'

    result = longest_common_substring(test_str1, test_str2)
    print(result)
