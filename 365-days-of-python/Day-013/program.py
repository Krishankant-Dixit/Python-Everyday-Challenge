# Day 13 Python Program
    # Fibonacci Sequence
n = int(input())
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a+b