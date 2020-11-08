# for 循环，计算1-100以内的奇数之和(i % 2 == 1), 偶数之和（i % 2 == 0）
total0 = 0
total1 = 0
for i in range(1, 101):
    if i % 2 == 1:
        total0 += i
    elif i % 2 == 0:
        total1 += i
print(total0)
print(total1)


# 另一种写法 - sum函数 + 推倒式
print(sum(i for i in range(1, 101) if i % 2 == 1))
print(sum(i for i in range(1, 101) if i % 2 == 0))


# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d x %d = %d" % (i, j, i*j))
    print()


# 打印九九乘法表 - 格式化
for i in range(1, 10):
    str1 = ''
    for j in range(1, i+1):
        str1 += str(i) + "x" + str(j) + "=" + str(i*j) + "  "
    print(str1)
