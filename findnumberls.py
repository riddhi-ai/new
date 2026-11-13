def linear_search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


numbers = [12, 5, 8, 20, 3]
target = int(input("Enter the number to find: "))

position = linear_search(numbers, target)

if position == -1:
    print("Number not found")
else:
    print("Found at index:", position)