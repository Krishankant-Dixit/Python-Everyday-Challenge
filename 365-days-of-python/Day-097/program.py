# Day 97 Python Program

        # Decryption
text = input("Enter encrypted text: ")

decrypted = ""

for char in text:
    decrypted += chr(ord(char) - 3)

print("Decrypted:", decrypted)