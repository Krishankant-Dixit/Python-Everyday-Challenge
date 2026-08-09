# Day 90 Python Program

        # Utility Package

# math_utils.py
def square(n):
    return n * n


# string_utils.py
def reverse(text):
    return text[::-1]


# main.py
from utils.math_utils import square
from utils.string_utils import reverse

print(square(10))
print(reverse("Python"))