def remove_duplicates(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique


numbers = [4, 2, 4, 7, 2, 9]
print("Without duplicates:", remove_duplicates(numbers))