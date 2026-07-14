# Day 55 Python Program

        # Phone Book
phonebook = {}

for i in range(3):
    name = input("Name: ")
    number = input("Phone: ")
    phonebook[name] = number

search = input("Search Name: ")

print(phonebook.get(search, "Contact Not Found"))