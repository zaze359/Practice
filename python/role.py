#!/usr/bin/python3

class Role():
    """角色"""

    # 表示构造函数，固定命名；形参self必须位于首位，它是指向实例本身的引用，会自动传递。
    def __init__(self, name, weapon, rarity, vision) -> None:
        """初始化"""
        self.name = name
        self.weapon = weapon
        self.rarity = rarity
        self.vision = vision
        # 属性添加默认值
        self.level = 1

    def get_name(self):
        return self.name

    # 定义的函数也需要 self参数
    def to_str(self):
        """输出类信息"""
        return "Role{"\
            "name=" + self.name + \
            ", weapon=" + self.weapon + \
            ", rarity=" + str(self.rarity) + \
            ", vision=" + self.vision + \
            ", level=" + str(self.level) + \
            "}"


class A():

    def __init__(self, a):
        self.a = a

    def p(self):
        print("a=" + self.a)


# B 继承 A
class B(A):

    def __init__(self, a, b):
        # 首先需要初始化父类
        super().__init__(a)
        self.b = b

    # 重写
    def p(self):
        print("a=" + self.a + "; b=" + self.b)


# a = A("a")
# b = B("a", "b")

# a.p()
# b.p()
