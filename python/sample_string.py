# coding=UTF-8

print("测试")

# 定义变量 message
message = "hello Python world" + "!"
# 输出
print(message)
print(message.title())
print(message.upper())
print(message.lower())

# 删除末尾空白：rstrip
language = "python "
print(language.rstrip() + "。")
print(language + "。")
# 并没有修改原值，需要重新赋值
language = language.rstrip()
print(language + "。")

# 字符串多行写法
language = "python"\
    "," + "java," + \
    "c++"
print(language)

# 多行字符串，且保留内部格式
lines = '''
第一行
第二行
第三行
'''
print(lines)
