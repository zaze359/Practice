#!/usr/bin/python3
# 定义函数
def say(message="world"):
    """这是函数的注释说明"""
    print("hello " + message)

# 使用默认值
say()
# 位置传参
say("java world")
# 命名参数
say(message="python world")

# -------
# 返回值
def get_role_name():
    return "胡桃"

print(get_role_name())

# -------
# 允许传递任意实参
def print_more(*messages):
    buffer = ""
    for msg in messages:
        buffer += msg
        buffer += " "
    print(buffer)

print_more("python", "world")

# -------
# 任意数量的 键值对 数据
def build_profile(**kv):
    print(kv)
    profile = {}
    for key, value in kv.items():
        profile[key] = value

    return profile

print(build_profile(name="胡桃", rarity=5))
