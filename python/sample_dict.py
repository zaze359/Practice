#!/usr/bin/python3
# 定义字典
role = {'name': "胡桃", 'weapon': '长枪'}

print(role['name'])
print(role['weapon'])

# 添加新的 键值对
role['vision'] = "火元素"
role['rarity'] = 5
role['unknow'] = "unknow"
print(role)

# 删除
del role['unknow']
print(role)


# 遍历
for key, value in role.items():
    print("\nKey: " + key)
    print("Value: " + str(value))

# 遍历key ：for key in role:  默认遍历的就是 key
for key in role.keys():
    print("Key: " + key)

# 遍历value
for key in role.values():
    print("Value: " + str(value))