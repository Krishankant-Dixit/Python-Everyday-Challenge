# Day 96 Python Program

        # Encryption
text = input("Enter text: ")

encrypted = ""

for char in text:
    encrypted += chr(ord(char) + 3)

print("Encrypted:", encrypted)