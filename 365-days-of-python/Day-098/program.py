# Day 98 Python Program

        # Caesar Cipher
text = input("Enter text: ")
shift = 3

result = ""

for char in text:

    if char.isalpha():
        base = ord("A") if char.isupper() else ord("a")
        result += chr((ord(char) - base + shift) % 26 + base)

    else:
        result += char

print("Encrypted:", result)