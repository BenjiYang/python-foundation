###################################################### 内置函数 ######################################################
# range()
range(10)
# list()
list(range(10))
# (start, stop, step)
list(range(0, 10, 2))
list(range(1, 10, 2))

# enumerate
print("同时取索引和值 ->  %s: " % list(enumerate([1, 3, 5, 7, 9])))
# id
# type
# isinstance
print(isinstance("hello", str))
# ord / chr
# len
# sum
print(sum([2, 4, 6]))
# max / min
print(max([1, 2, 3, 4]))
print(min([1, 2, 3, 4]))
# 取平均数
list1 = [1, 3, 5, 7, 9]
print(len(list1))
print(sum(list1))
print(sum(list1)/len(list1))
# sorted - 排序生成新的列表，与sort区别，sort还是原来那个指针
print(sorted([3, 2, 5, 4, 1, 7]))
# reversed
print(list(reversed([3, 2, 5, 4, 1, 7])))
# zip
###################################################### 内置函数 ######################################################
