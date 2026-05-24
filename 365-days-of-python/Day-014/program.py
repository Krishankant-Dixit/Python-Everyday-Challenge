# Day 14 Python Program
    # Prime Number
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

print("Prime" if flag else "Not Prime")