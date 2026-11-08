def reverse_number(n):
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    return reversed_num


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter 0 or a positive integer.")
else:
    print("Reversed number:", reverse_number(number))