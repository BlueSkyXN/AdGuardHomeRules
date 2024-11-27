import os

filenames = [
    "Renew/cjx-annoyance.txt",
    "Renew/anti-ad-adguard.txt",
    "Renew/anti-ad-easylist.txt",
    "Renew/easyprivacy.txt",
    "Renew/easylist.txt",
    "Renew/easylistchina.txt",
    "Renew/halflife.txt",
    "Renew/scamblocklist-host.txt",
    "Renew/AWAvenue-Ads-Rule.txt",
    "Renew/StevenBlack.txt"
]

output_filename = 'Part/rules-renew.txt'

with open(output_filename, 'w', encoding='utf-8') as outfile:
    for fname in filenames:
        with open(fname, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())

print(f"Files merged and saved at: {os.path.abspath(output_filename)}")
