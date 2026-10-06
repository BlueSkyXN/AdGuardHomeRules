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
            content = infile.read()
        outfile.write(content)
        # 部分上游文件（如 easylistchina.txt）末尾没有换行符，
        # 直接拼接会让下一文件的首行粘在本文件末行之后，产生形如
        # "!---The End---![Adblock Plus 2.0]" 的非法规则行。
        # 这里统一补一个换行，保证文件之间正确分隔。
        if content and not content.endswith('\n'):
            outfile.write('\n')

print(f"Files merged and saved at: {os.path.abspath(output_filename)}")
