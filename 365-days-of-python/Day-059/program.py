# Day 59 Python Program

        # Menu Driven Dictionary App
student = {}

while True:

    print("\n1. Add")
    print("2. View")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = input("Key: ")
        value = input("Value: ")
        student[key] = value

    elif choice == 2:
        print(student)

    elif choice == 3:
        break