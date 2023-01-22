#!/usr/bin/python3

filename = r'./res/test.txt'

# with 不再需要访问文件后会将其关闭。
# 读取全部
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("-------------------------")

# 读取到列表中
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

print("-------------------------")

# 逐行读取
with open(filename) as file_object:
    for line in file_object:
        # 逐行读取时，末尾会有一个换行符。通过 rstrip 去除。
        print(line.rstrip())

# 文件写入
write_filename = "./res/write.txt"

# r: 只读模式，默认
# w: 写入模式
# r+: 读写模式
# a: 附加模式，往末尾写入
with open(write_filename, "w") as file_object:
    file_object.write("Hello Python")
