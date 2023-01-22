#!/usr/bin/python3

names = ["胡桃", '甘雨', '宵宫']

# in 是否在列表内
print("胡桃" in names)

# and 并且
print("胡桃" in names and "甘雨" in names)

# or 或
print("胡桃" in names or "丘丘人" in names)


# 遍历
print("------- 遍历 for in : -------")
for name in names:
    print(name)

print("------- 遍历 for in range: -------")
# 左闭右开 区间：输出 1,2,3,4
for name in range(1, 5):
    print(name)


names = []
# if-elif-else
if names:
    print("有数据")
else:
    print("无数据，添加数据")
    names = ["胡桃", '甘雨', '宵宫']


if "丘丘人" in names:
    print("丘丘人")
elif "胡桃" in names:
    print("胡桃")
else:
    print("无")


print("------------------")

count = 3
while count > 0:
    print(count)
    count -= 1


print("------------------")
while True:
    print(count)
    count += 1
    if count == 2:
        count += 2
        continue
    if count > 3:
        break

print("------------------")
