# 1-100 list 手写
myList = []
for i in range(1, 101):
    if i % 2 == 1:
        myList.append(i)
print(myList)

# 1-100 list 推导式写法
print([i for i in range(1, 101) if i % 2 == 1])


# 练习：筛选出100以内能被2整除，同时大于10 的整数列表
print([i for i in range(1, 101) if i % 2 == 0 if i > 10])
print([i for i in range(11, 101) if i % 2 == 0])

# 练习2: 1-10 内的偶数为x, 2^^x
print([2**i for i in range(1, 11) if i % 2 == 0])
