###################################################### 数据类型 dictionary 字典 ######################################################
# Create
myDict1 = {}
myDict1 = {"name": 'Alice', "age": 22, "sex": 'female'}


# Update - dict[key] = value -- 修改原有数据:
myDict1['name'] = 'Anny'
print("myDict1['name'] = 'Anny' -> %s" % myDict1)

# Update - dict[new key] = value -- 添加未含有的数据:
myDict1["weight"] = 60
print('myDict1["weight"] = 60 -> %s' % myDict1)

# Update - dic1.update(dic2) - dic2插入到dic1并复写重复键值
aggregateDict1 = {"name": "Alex", "age": 21, "weight": 175}
aggregateDict2 = {"name": "Ben", "age": 30, "sex": "male"}
print("before - aggregateDict1 - %s" % aggregateDict1)
print("before - aggregateDict2 - %s" % aggregateDict2)
aggregateDict1.update(aggregateDict2)  # 更新aggregateDict1 - 传入的其他字典值插入复写
print("after - aggregateDict1 - %s" % aggregateDict1)
print("after - aggregateDict2 - %s" % aggregateDict2)


# Read - dict[key]
print(myDict1["name"])

# Read - dict.keys() -- 只取keys:
print(myDict1.keys())

# Read - dict.values() -- 只取values:
print(myDict1.values())

# Read - dict.items() -- 取所有 items
print(myDict1.items())


# pop - dict.pop[key] -- 栈操作，后进先出:
print('---------------------- PoP Action ---------------------- %s' % myDict1)
myDict1.pop("sex")
print('myDict1.pop("sex") -> %s' % myDict1)

# clear - 保留指针
myDict1.clear
print('myDict1.clear -> %s' % myDict1)

# Delete - 清除痕迹
del myDict1
###################################################### 数据类型 dictionary 字典 ######################################################
