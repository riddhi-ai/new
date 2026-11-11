def second_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    second = None

    for number in numbers:
        if number < largest:
            if second is None or number > second:
                second = number

    return second


numbers = [10, 20, 20, 8, 15]
answer = second_largest(numbers)

if answer is None:
    print("No second-largest distinct number")
else:
    print("Second largest:", answer)