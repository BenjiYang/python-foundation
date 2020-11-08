import json


demo_dict = {"name": "Tom", "age": 50}
print(type(demo_dict))
# json.dumps(dict) 字典序列化
ret_json = json.dumps(demo_dict)
print(type(ret_json))
print(ret_json)

# json.loads(dict) 字典反序列化
ret_de_json = json.loads(ret_json)
print(type(ret_de_json))
print(ret_de_json)
