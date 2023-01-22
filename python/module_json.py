import json


filename = "./res/numbers.json"

numbers = [1, 3, 5, 7, 9]
with open(filename, "w") as f_obj:
    json.dump(numbers, f_obj)


with open(filename, "r") as f_obj:
    read_nums = json.load(f_obj)

print(read_nums)
