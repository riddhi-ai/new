def reverse_string(text):
    result = ""

    for character in text:
        result = character + result

    return result


text = input("Enter a string: ")
print("Reversed:", reverse_string(text))