'''
size array
elements

(value, frequency, percentage)
'''
def return_ave_freq_perc(arr):
    values = list(set(arr)) # removes
    frequency = [arr.count(i) for i in values]
    percentage = [(frequency[i] / len(values)) * 100 for i in range(len(values))]

    print(f"Values: {values}, Frequency: {frequency}, Percentage: {percentage}")
    for i in range(len(values)):
        print(f"({values[i]}, {frequency[i]}, {percentage[i]:.2f})")


def main():
    size = int(input("Enter size of array: "))
    print("Enter elements of array: ")

    arr = []
    for i in range(size):
        ele = int(input())
        arr.append(ele)

    print()
    return_ave_freq_perc(arr)

if __name__ == '__main__':
    main()
