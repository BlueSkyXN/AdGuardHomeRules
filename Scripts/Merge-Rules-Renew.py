import os

# 定义文件名列表
filenames = ["cjx-annoyance.txt", "anti-ad-adguard.txt", "anti-ad-easylist.txt", "easyprivacy.txt", "easylist.txt", "easylistchina.txt", "halflife.txt", "scamblocklist-host.txt", "StevenBlack.txt"]

# 打开你想要写入的文件
with open("Part/rules-renew.txt", 'w') as outfile:
    # 遍历文件名列表
    for fname in filenames:
        # 为每个文件名创建完整路径
        path = os.path.join("Renew", fname)
        # 打开每个文件
        with open(path) as infile:
            # 读取文件内容并写入新文件
            outfile.write(infile.read())
        # 在每个文件之间添加一个换行符，以确保文件的内容不会混在一起
        outfile.write("\n")
