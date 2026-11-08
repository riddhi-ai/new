def factorial(n):
    result = 1

    for number in range(1, n + 1):
        result *= number

    return result


n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined here for negative numbers.")
else:
    print("Factorial:", factorial(n))