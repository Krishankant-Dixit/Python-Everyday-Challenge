# Day 53 Python Program

        # Student Marks System
marks = {}

for i in range(5):
    subject = input("Enter Subject: ")
    score = int(input("Enter Marks: "))
    marks[subject] = score

print("\nResult")

for subject, score in marks.items():
    print(subject, ":", score)