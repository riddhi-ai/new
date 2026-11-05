#largest without max()
def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


print(find_largest([4, 9, 2, 11, 6]))