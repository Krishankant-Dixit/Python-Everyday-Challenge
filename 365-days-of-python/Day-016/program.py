# Day 16 Python Program
    # Palindrome Number
num = int(input())
temp = num
rev = 0

while num > 0:
    rev = rev*10 + num%10
    num //= 10

print("Palindrome" if temp == rev else "Not Palindrome")