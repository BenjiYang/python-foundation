# list.sort() -- 列表元素排序 - 正序:
numlistSort = [1, 3, 4, 2, 6, 5, 7]
print('numlistSort - %s' % numlistSort)
numlistSort.sort()
print("numlistSort.sort() -> numlistSort - %s" % numlistSort)

# list.sort(reverse=True) -- 列表元素排序 - 逆序:
numlistReverse = [1, 3, 4, 2, 6, 5, 7]
print('numlistReverse - %s' % numlistReverse)
numlistReverse.sort(reverse=True)
print("numlistReverse.sort() -> numlistReverse - %s" % numlistReverse)


# ================================== 类型转换 手写函数 ==================================

convertListStr2IntSortList = ['1', '3', 4, '2', 6, 5, 7]
# 期望排序后结果['1', '2', '3', 4, 5, 6, 7]
# 先定义一个 str -> int 的类型转换函数


def ret_int(item):
    return int(item)


# 正序 list.sort(key=ret_int) -- 把list每个index key的值，通过自定义的方法先转换成整型，然后再计算排序
convertListStr2IntSortList.sort(key=ret_int)
print("convertListStr2IntSortList.sort(key=ret_int) -> convertListStr2IntSortList - %s" %
      convertListStr2IntSortList)


# 逆序 list.sort(key=ret_int, reverse=True) -- 把list每个index key的值，通过自定义的方法先转换成整型，然后再计算排序
convertListStr2IntSortList.sort(key=ret_int, reverse=True)
print("convertListStr2IntSortList.sort(key=ret_int, reverse=True) -> convertListStr2IntSortList - %s" %
      convertListStr2IntSortList)
# ================================== 类型转换 手写函数 ==================================
