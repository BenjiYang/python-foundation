
###################################################### 字典排序方式1 - 手写方法 ######################################################
apple = {"goods": "apple", "price": 8}
pear = {"goods": "pear", "price": 2}
orange = {"goods": "orange", "price": 4}
fruit = [apple, pear, orange]


def dict_helper(item):
    return item["price"]


fruit.sort(key=dict_helper)
print(fruit)
###################################################### 字典排序方式1 - 手写方法 ######################################################
