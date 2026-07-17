# Day 60 Python Program

        # Contact Book Project
contacts = {}

while True:

    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Exit")

    choice = int(input("Choice: "))

    if choice == 1:

        name = input("Name: ")
        phone = input("Phone: ")

        contacts[name] = phone

    elif choice == 2:

        name = input("Search Name: ")

        print(contacts.get(name, "Not Found"))

    elif choice == 3:

        print(contacts)

    elif choice == 4:

        break