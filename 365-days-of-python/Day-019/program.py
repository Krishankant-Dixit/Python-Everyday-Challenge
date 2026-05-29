# Day 19 Python Program

        # GCD
a = int(input())
b = int(input())

while b:
    a, b = b, a % b

print("GCD:", a)