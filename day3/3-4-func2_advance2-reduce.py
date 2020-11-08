# 高阶函数

from functools import reduce

# reduce -- 1+2+3+4+10
reduce_obj_1 = reduce(lambda x, y: x+y, [1, 2, 3, 4, 10])
print(reduce_obj_1)


# reduce -- 1*2*4 =8
reduce_obj_2 = reduce(lambda x, y: x*y, [1, 2, 4])
print(reduce_obj_2)
