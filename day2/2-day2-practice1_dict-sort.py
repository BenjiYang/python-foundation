''' 练习1 - {'apple':10, 'banana':4, 'pear':5} 排序
定义一个字典fruit = {'apple':10, 'banana':4, 'pear':5}
输出字典的每一个key和value，按照从小到大排序
ref: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
'''
# 方式1 - v3.6+ same as 方式2
fruit = {'apple': 10, 'banana': 4, 'pear': 5}
print({k: v for k, v in sorted(fruit.items(), key=lambda item: item[1])})

# 方式2 list type -> sorted(fruit.items(), key=lambda item: item[1]
fruit = {'apple': 10, 'banana': 4, 'pear': 5}
sorted_fruit = dict(sorted(fruit.items(), key=lambda item: item[1]))
print(sorted_fruit)

# 方式3 list type -> sorted(fruit.items(), key=lambda kv: kv[1])
fruit = {'apple': 10, 'banana': 4, 'pear': 5}
sorted_fruit = dict(sorted(fruit.items(), key=lambda kv: kv[1]))
print(sorted_fruit)
