def print_x(n = 5):
    for i in range(n):
        for j in range(n):
            if (i == j) or i== (n - 1 - j):
                print("*", end='')
            else:
                print(" ", end='')
        print()

print_x()
