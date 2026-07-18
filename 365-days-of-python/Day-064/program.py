# Day 64 Python Program

        # Count words in a File
file = open("sample.txt", "r")

data = file.read()

words = data.split()

print("Total Words:", len(words))

file.close()