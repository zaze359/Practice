#!/usr/bin/python3

filename = "a.txt"
# filename = "./res/test.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    # 发生异常
    print("file not found")
else:
    # 正常流程到后续
    print(contents)
