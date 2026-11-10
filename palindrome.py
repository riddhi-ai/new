def is_palindrome(text):
    text = text.lower()
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return text == reversed_text


text = input("Enter a word: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")