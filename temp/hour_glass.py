def print_hourglass(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Print stars for the top half
        for j in range(2 * i - 1):
            print("*", end="")

        print()  # Move to the next line

    for i in range(2, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")

        # Print stars for the bottom half
        for j in range(2 * i - 1):
            print("*", end="")

        print()  # Move to the next line

# Example usage with 5 rows
print_hourglass(5)
