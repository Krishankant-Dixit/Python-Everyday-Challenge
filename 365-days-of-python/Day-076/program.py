# Day 76 Python Program

        # Divide Calculator
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Enter valid numbers")