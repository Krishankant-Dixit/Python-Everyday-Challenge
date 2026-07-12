# Day 50 Python Program

        # Password Generator
import random
import string

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(10):

    password += random.choice(chars)


print(password)