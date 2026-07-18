# Day 66 Python Program

        # Copy File
source = open("sample.txt", "r")

data = source.read()

source.close()

destination = open("copy.txt", "w")

destination.write(data)

destination.close()

print("File Copied Successfully.")