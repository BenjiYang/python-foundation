# ================================== 类型转换 手写转换 ==================================
myList = [1, 3, '5', '7', 9, 2, 4, 6, 99, 88, 0, None, 100]
print(type(myList[6]) == str and not myList[6].isdigit)


def deal_item(item):
    # 如果是int类型，无需处理，直接返回
    if isinstance(item, int):
        return item
    # 如果str类型，且是数字，转换成int后返回
    if isinstance(item, str) and item.isdigit:
        return int(item)
    # 其他 - 终止跳过
    return 0


myList.sort(key=deal_item, reverse=True)
print(myList)
# ================================== 类型转换 手写转换 ==================================
