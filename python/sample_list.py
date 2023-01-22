#!/usr/bin/python3

# 创建
digits = list(range(1, 5))
print(digits)

# 可以是不同类型
names = ("胡桃", 1, 2)
print(names)
# 
names = ["胡桃", '甘雨', '宵宫']
print(str(names) + " 长度: " + str(len(names)))

# 读取
print("------- 读取 -------")
print("0 访问最后一个：" + names[0])
# 访问最后一个，列表为空时会报错
print("-1 访问最后一个：" + names[-1])
# 开始位置：index，0可省略
# 结束位置：index + 1
print("前2个: " + str(names[0:2]))
print("第二个到末尾" + str(names[1:]))
# -2 表示后2个
print("后2个" + str(names[-2:]))

# 复制
print("------- 复制 -------")
names2 = names[:]
names2.append("我是复制到")
print(names2)
print(names)

# 修改
print("------- 修改-------")
names[0] = "神里绫华"
print(names)

# 添加
print("------- 添加 append -------")
names.append("胡桃")
print(names)

# 插入
print("------- 插入 insert -------")
names.insert(1, "丘丘人")
print(names)

# 删除
print("------- 删除 del, remove -------")
del names[1]
print(names)
names.append("蕈兽")
print(names)
names.remove("蕈兽")
print(names)

# pop
print("------- pop -------")
sl = names.pop()
print(sl)
print(names)

# 排序
print("------- 临时排序 sorted -------")
print(sorted(names))
print(names)
print("------- 永久排序 sort -------")
# 内部值被修改
names.sort()
print(names)

# 反转列表
print("------- 反转列表 reverse -------")
# 修改了内部值
names.reverse()
print(names)

# 遍历
print("------- 遍历 for in : -------")
for name in names:
    print(name)

print("------- 遍历 for in range: -------")
# 左闭右开 区间：输出 1,2,3,4
for name in range(1, 5):
    print(name)


# 计算
print("------- 列表计算 min, max, sum: -------")
print(digits)
print("min: " + str(min(digits)))
print("max: " + str(max(digits)))
print("sum: " + str(sum(digits)))

# 列表解析
print("------- 列表解析 [表达式 for循环提供值 ] -------")
# **2 平方
squares = [value**2 for value in range(1, 11)]
print(squares)


# 元组
names = ("胡桃", '甘雨', '宵宫')
print(names)
# names[0] = "丘丘人" 不能修改
names = ('宵宫')  # 变量可以重新赋值
print(names)
