# list vs tuple
# 比较内存空间使用，tuple相较于list使用更少空间
listSpace = list(range(3))
tupleSpace = tuple(range(3))
print(listSpace)
print('listSpace.__sizeof__() - %s' % listSpace.__sizeof__())
print(tupleSpace)
print('tupleSpace.__sizeof__() - %s' % tupleSpace.__sizeof__())

# 比较性能，tuple相较于list使用性能更高
''' Run in cmd with ipython
In [1]: %timeit x1 = [1, 2, 3]
10000000 loops, best of 3: 134 ns per loop

In [2]: %timeit t1 = (1, 2, 3)
100000000 loops, best of 3: 16.5 ns per loop
'''
