# Day 80 Python Program

        # Login System
username = "admin"
password = "1234"

try:
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login successful")

    else:
        print("Invalid username or password")

except Exception as e:
    print("Error:", e)