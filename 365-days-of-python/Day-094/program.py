# Day 94 Python Program

        # Text Analyzer
text = input("Enter text: ")

words = text.split()
characters = len(text)
spaces = text.count(" ")

print("Characters:", characters)
print("Words:", len(words))
print("Spaces:", spaces)