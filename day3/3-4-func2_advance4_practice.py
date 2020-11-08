# map -- 非数字类型处理为0， None处理为0
unsorted_list = [9, 18, 64, 88, 66, 72, 2, None, 'c']
map_obj = map(lambda x: x if isinstance(x, int) else 0, unsorted_list)
print(list(map_obj))

# filter -- 筛选出所有偶数
list_a = [1, 4, 12, 9]
filter_obj = filter(lambda x: x % 2 == 0, list_a)
print(list(filter_obj))
