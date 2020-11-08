# ================================== list slice ==================================
# 快速生成 0～9 的一个列表
numlist = list(range(10))

print('list(range(10)) - %s' % numlist)

print('numlist[-2:] - %s' % numlist[-2:])
print('numlist[8:10] - %s' % numlist[8:10])


# some_list[start:stop:step]
# 从start key=1，没有天终止key，step=2
print('numlist[1::2] - %s' % numlist[1::2])
print('numlist[1:6:2] - %s' % numlist[1:6:2])
print('numlist[::-1] - %s' % numlist[::-1])
# ================================== list slice ==================================
