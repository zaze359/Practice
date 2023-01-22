#!/usr/bin/python3

import unittest
from role import Role

# 需要继承 TestCase
class TestRole(unittest.TestCase):
    """测试用例"""

    def setUp(self) -> None:
        """创建所有测试用例 共用的数据"""
        self.role = Role(name="胡桃", weapon="长枪", rarity=5, vision="火")

    def test_get_name(self):
        """单元测试"""
        hutao = self.role
        # 断言
        self.assertEqual(hutao.name, hutao.get_name())

# 执行测试
unittest.main()
