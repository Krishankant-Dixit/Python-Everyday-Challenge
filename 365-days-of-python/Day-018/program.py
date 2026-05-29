# Day 18 Python Program

        # Armstrong Number
num = int(input())
temp = num
sum_ = 0

while num > 0:
    digit = num % 10
    sum_ += digit**3
    num //= 10

print("Armstrong" if temp == sum_ else "Not Armstrong")