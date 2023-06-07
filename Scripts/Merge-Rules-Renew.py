filenames = [
    "Renew/cjx-annoyance.txt",
    "Renew/anti-ad-adguard.txt",
    "Renew/anti-ad-easylist.txt",
    "Renew/easyprivacy.txt",
    "Renew/easylist.txt",
    "Renew/easylistchina.txt",
    "Renew/halflife.txt",
    "Renew/scamblocklist-host.txt",
    "Renew/StevenBlack.txt"
]

with open('Part/rules-renew.txt', 'w', encoding='utf-8') as outfile:
    for fname in filenames:
        with open(fname, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
