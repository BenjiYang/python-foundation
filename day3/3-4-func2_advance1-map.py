# 高阶函数 map reduce --- 大数据使用这类算法 分布式 多台性能普通的机器做运算 集群 处理

from functools import reduce

# ipython 查看说明 如： map??
map_obj_1 = map(int, ['1', '2', 3, 4, '5'])
print(list(map_obj_1))

map_obj_2 = map(lambda x: x**2, range(10))
print(list(map_obj_2))
