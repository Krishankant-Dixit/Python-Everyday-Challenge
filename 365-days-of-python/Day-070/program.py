# Day 70 Python Program

        # Notes Manager Project
while True:

    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        note = input("Write Note: ")

        file = open("notes.txt", "a")

        file.write(note + "\n")

        file.close()

    elif choice == 2:

        file = open("notes.txt", "r")

        print("\nYour Notes:\n")

        print(file.read())

        file.close()

    elif choice == 3:

        break