# Day 78 Python Program

        # Input Validation
while True:

    try:
        num = int(input("Enter a number: "))
        print("Valid input:", num)
        break

    except ValueError:
        print("Please enter a valid integer")