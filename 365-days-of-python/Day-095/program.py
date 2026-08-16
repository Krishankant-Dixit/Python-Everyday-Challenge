# Day 95 Python Program

        # Character Frequency
text = input("Enter text: ")

frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

for char, count in frequency.items():
    print(char, ":", count)