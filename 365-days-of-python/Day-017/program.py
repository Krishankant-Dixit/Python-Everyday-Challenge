# Day 17 Python Program

        # Sum of digits
num = int(input())
sum_ = 0

while num > 0:
    sum_ += num % 10
    num //= 10

print(sum_)