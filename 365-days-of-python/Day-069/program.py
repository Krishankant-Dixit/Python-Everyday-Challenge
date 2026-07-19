# Day 69 Python Program

        # Student Record System
file = open("students.txt", "a")

name = input("Enter Name: ")
marks = input("Enter Marks: ")

file.write(name + " : " + marks + "\n")

file.close()

print("Record Saved Successfully.")