import os

input_filename = "all.txt"
filename = "all-lite.txt"

with open(input_filename, "r", encoding='utf-8') as f:
    lines = f.readlines()

# Remove lines that start with '!'
lines = [line for line in lines if not line.startswith('!')]

# Remove duplicates and write back to file.
# 注意：不要直接 writelines(set(lines))。Python 的 str 哈希默认随机化
# （PYTHONHASHSEED），set 的迭代顺序在不同进程之间不一致，会导致每次运行
# 生成的 all-lite.txt 行序都不同，产生整文件级别的无意义 diff。
# 这里改用「保序去重」，输出结果稳定可复现。
seen = set()
unique_lines = []
for line in lines:
    if line not in seen:
        seen.add(line)
        unique_lines.append(line)

with open(filename, "w", encoding='utf-8') as f:
    f.writelines(unique_lines)

print(f"File saved at: {os.path.abspath(filename)}")
print(f"Input lines: {len(lines)}, unique lines: {len(unique_lines)}")
