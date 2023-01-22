from collections import OrderedDict

dicts = OrderedDict()

dicts["key1"] = "value1"
dicts["key2"] = "value2"
dicts["key3"] = "value3"

for key, value in dicts.items():
    print(key + "=" + value)