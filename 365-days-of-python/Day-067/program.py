# Day 67 Python Program

        # Search word
file = open("sample.txt", "r")

data = file.read()

word = input("Enter word to search: ")

if word in data:
    print("Word Found")
else:
    print("Word Not Found")

file.close()