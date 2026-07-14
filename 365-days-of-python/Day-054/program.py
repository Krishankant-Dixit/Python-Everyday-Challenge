# Day 54 Python Program

        # Word Frequency Counter
sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)