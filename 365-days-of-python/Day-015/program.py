# Day 15 Python Program
    # Reverse Number
num = int(input())
rev = 0

while num > 0:
    rev = rev*10 + num%10
    num //= 10

print("Reverse:", rev)