###################################################### 字典排序方式2 - lambda ######################################################
# list.sort(key=lambda x: x[aKeyName])
apple = {"goods": "apple", "price": 8}
pear = {"goods": "pear", "price": 2}
orange = {"goods": "orange", "price": 4}
fruit = [apple, pear, orange]
fruit.sort(key=lambda x: x["price"])
print(fruit)
###################################################### 字典排序方式2 - lambda ######################################################
