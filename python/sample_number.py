# coding=UTF-8
num = 3 + 0.1
print(num)

# string 转 int
num = 3 + int('21')
print(num)

# 数字和字符串 拼接时需要使用 `str()` 进行类型转换，否则会触发 `TypeError` 异常
print("num = " + str(num)) 