# Day 79 Python Program

        # ATM Simulation
balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient balance")

    else:
        balance -= amount
        print("Withdraw successful")
        print("Remaining balance:", balance)

except ValueError:
    print("Enter valid amount")