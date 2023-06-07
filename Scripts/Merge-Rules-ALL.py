import os

filenames = [
    "Part/rules-renew.txt",
    "Part/rules-classic.txt"
]

output_filename = 'all.txt'

with open(output_filename, 'w', encoding='utf-8') as outfile:
    for fname in filenames:
        with open(fname, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())

print(f"Files merged and saved at: {os.path.abspath(output_filename)}")
