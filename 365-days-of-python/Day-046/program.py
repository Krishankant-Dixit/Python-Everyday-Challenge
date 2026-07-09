# Day 46 Python Program

        # Count Upper & Lower Case
s = input()

upper = 0
lower = 0

for ch in s:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1


print("Upper =", upper)
print("Lower =", lower)