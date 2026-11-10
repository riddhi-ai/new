def count_vowels(text):
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count += 1

    return count


text = input("Enter a string: ")
print("Vowel count:", count_vowels(text))