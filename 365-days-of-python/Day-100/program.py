# Day 100 Python Program

        # Text Statistics
text = input("Enter text: ")

words = text.split()

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text:

    if char.lower() in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    elif char.isspace():
        spaces += 1


print("Characters:", len(text))
print("Words:", len(words))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)