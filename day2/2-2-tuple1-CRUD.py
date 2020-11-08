###################################################### 数据类型 tuple 元组 ######################################################
# 元组与列表类似，不同在于元组元素不能修改
# 元组使用 (), 列表使用 []

# Create
emptyTuple = ()
print(emptyTuple)

# type(tuple) -- Type of the tuple <class 'tuple'>
print('type((1, 2)) - %s' % type((1, 2)))

# Create with range() method
numTuple1 = tuple(range(10))
print(numTuple1)
print(id(numTuple1))
# 再赋值一遍，元组id会改变
numTuple1 = tuple(range(10))
print(id(numTuple1))


# Read
tupleHybrid = (10, 5, "Alice", [1, 3, 5, 7])
print('type(tupleHybrid) - %s' % type(tupleHybrid))
print('len(tupleHybrid) - %s' % len(tupleHybrid))


# https://stackoverflow.com/questions/1455602/printing-tuple-with-string-formatting-in-python
# Making a singleton tuple with the tuple of interest as the only item, i.e. the (thetuple,) part, is the key bit here.
print('Read - tupleHybrid - %s' % (tupleHybrid,))
print('Read - tupleHybrid[1] - %s' % tupleHybrid[1])
print('Read - tupleHybrid[2] - %s' % tupleHybrid[2])
print('Read - tupleHybrid[3] - %s' % tupleHybrid[3])

# Read - tuple.index(value) -- return index
print("tupleHybrid.index('Alice') - %s" % tupleHybrid.index('Alice'))
# Read - tuple[index] -- return value
print(tupleHybrid[1])

# Convertion - tuple(list) -- list转换成tuple：
myList = list(range(10))
print('mylist - %s' % myList)
myListConverted2Tuple = tuple(myList)
print('tuple(myList) - %s' % (myListConverted2Tuple,))


# 元组拼接 - 字符串拼接，数字四则运算等
tup1 = (20)
tup2 = (30)
tup3 = tup1 + tup2
print(tup3)


# 删除元组
del people_tuple
###################################################### 数据类型 tuple 元组 ######################################################
