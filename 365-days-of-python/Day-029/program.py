# Day 29 Python Program

        # Count Vowels in String
s = input().lower()
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)