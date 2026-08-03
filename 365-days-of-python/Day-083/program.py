# Day 83 Python Program

        # datetime Module
from datetime import datetime

now = datetime.now()

print("Current Date & Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Time:", now.strftime("%H:%M:%S"))