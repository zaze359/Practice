#!/usr/bin/python3

# 导入整个模块
import hello as h
# 导入类
from role import Role

h.say("python")

hutao = Role(name="胡桃", weapon="长枪", rarity=5, vision="火")
print(hutao.to_str())



# 导入部分函数
# from hello import say
# say("python")