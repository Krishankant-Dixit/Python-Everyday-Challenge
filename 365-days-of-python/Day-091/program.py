# Day 91 Python Program

        # Regex Basics
import re

text = "Python is powerful and Python is easy."

matches = re.findall("Python", text)

print("Matches:", matches)
print("Count:", len(matches))