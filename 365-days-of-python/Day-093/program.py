# Day 93 Python Program

        # Password Validation
import re

password = input("Enter password: ")

if len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password):
    print("Valid Password")
else:
    print("Password must have 8+ characters, one uppercase letter and one number")