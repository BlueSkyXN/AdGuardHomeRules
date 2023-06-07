import os

with open("all.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()

# Remove lines that start with '!'
lines = [line for line in lines if not line.startswith('!')]

# Remove duplicates and write back to file
filename = "all-lite.txt"
with open(filename, "w", encoding='utf-8') as f:
    f.writelines(set(lines))

print(f"File saved at: {os.path.abspath(filename)}")
