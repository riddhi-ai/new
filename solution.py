def find_largest(numbers):
    """Return the largest number in a nonempty list."""
    if not numbers:
        raise ValueError("The list must not be empty.")

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


if __name__ == "__main__":
    examples = [
        [4, 9, 2, 11, 6],
        [-8, -3, -10],
        [5],
        [7, 7, 7],
    ]

    for numbers in examples:
        print(f"{numbers} -> {find_largest(numbers)}")