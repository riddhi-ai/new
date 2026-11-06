def count_even_odd(numbers):
    even = 0
    odd = 0

    for number in numbers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


numbers = [4, 7, 2, 9, 6]
even_count, odd_count = count_even_odd(numbers)

print("Even:", even_count)
print("Odd:", odd_count)