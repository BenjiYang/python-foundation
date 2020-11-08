# ================================== 类型转换 lambda ==================================
# 正序 list.sort(key=lambda x: int(x)) -- 使用Lambda转换类型后排序
convertListStr2IntSortList = ['1', '3', 4, '2', 6, 5, 7]
convertListStr2IntSortList.sort(key=lambda x: int(x))
print("convertListStr2IntSortList.sort(key=lambda x: int(x)) -> convertListStr2IntSortList - %s" %
      convertListStr2IntSortList)

# 逆序 list.sort(key=lambda x: int(x), reverse=True) -- 使用Lambda转换类型后排序
convertListStr2IntSortList.sort(key=lambda x: int(
    x), reverse=True)
print("convertListStr2IntSortList.sort(key=lambda x: int(x), reverse=True) -> convertListStr2IntSortList - %s" %
      convertListStr2IntSortList)
# ================================== 类型转换 lambda ==================================
