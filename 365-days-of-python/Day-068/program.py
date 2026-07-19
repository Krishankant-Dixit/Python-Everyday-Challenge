# Day 68 Python Program

        # Replace word in file
file = open("sample.txt", "r")

data = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

data = data.replace(old_word, new_word)

file.close()

file = open("sample.txt", "w")

file.write(data)

file.close()

print("Word Replaced Successfully.")