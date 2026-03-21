import os

base_folder = "365-days-of-python"

os.makedirs(base_folder, exist_ok=True)

for i in range(1, 366):
    folder_name = f"Day-{i:03d}"
    folder_path = os.path.join(base_folder, folder_name)
    
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, "program.py")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Day {i} Python Program\n")

# README with UTF-8 encoding
with open(os.path.join(base_folder, "README.md"), "w", encoding="utf-8") as f:
    f.write("# 365 Days of Python Challenge \n")

print("Structure created successfully!")