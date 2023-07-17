import os

def split_file(filename, chunk_size):
    # 创建子目录 /Part
    os.makedirs("Part", exist_ok=True)

    # 读取原始文件
    with open(filename, 'r') as file:
        data = file.read()

    # 计算切割后的子文件数量
    num_chunks = (len(data) + chunk_size - 1) // chunk_size

    # 切割并保存子文件
    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk_data = data[start:end]

        # 构建子文件名
        file_parts = os.path.splitext(filename)
        new_filename = os.path.join("Part", f"{file_parts[0]}-p{i+1}{file_parts[1]}")

        # 保存子文件
        with open(new_filename, 'w') as new_file:
            new_file.write(chunk_data)

        print(f"Created chunk file: {new_filename}")

# 指定要切割的文件和子文件大小（9MB）
file_to_split = "all-lite.txt"
chunk_size = 9 * 1024 * 1024

# 调用函数进行切割
split_file(file_to_split, chunk_size)
