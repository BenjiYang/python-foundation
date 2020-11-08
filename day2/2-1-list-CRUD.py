###################################################### 数据类型 list ######################################################
# pythondoc - http://www.pythondoc.com/pythontutorial3/datastructures.html?highlight=extend


# Create
createList = []
createList = ['Chinese', 'English', 'Chemistry']
print("createList - %s" % createList)


# Append - list.append(value)
appendList = ['A', 'B', 'C']
appendList.append(99)
appendList.append(createList)
print("appendList - %s" % appendList)


# Insert - list.insert(index, value)
insertList = [0, 1, 2]
insertList.insert(1, 'Inserted')
print("insertList - %s" % insertList)


# Read - list[index] --  Read via index:
readList = ['read1', 'read2', 'read3']
print('readList - %s' % readList)
print('readList[0] - %s' % readList[0])
print('readList[1] - %s' % readList[1])
print('readList[2] - %s' % readList[2])


# Update - list[index] =-  value - Via index to do value assign:
updateList = ['update1', 'update2']
print('updateList - %s' % updateList)
updateList[1] = 'AfterUpdateValue'
print("updateList[1] = 'AfterUpdateValue' -> updateList - %s" % updateList)


# Delete - del list[index] --  index正序计算来删除：
list2DeleteViaIndex = ['list2DeleteViaIndex1', 'list2DeleteViaIndex2']
print('list2DeleteViaIndex - %s' % list2DeleteViaIndex)
del list2DeleteViaIndex[0]
print(
    "del list2DeleteViaIndex[0] -> list2DeleteViaIndex - %s" % list2DeleteViaIndex)

# Delete - list.pop(index) --  当堆栈用，index逆序计算来删除:
# Delete - list.popleft(index) -- 当队列用，先进先出。
list2DeleteViaPop = ['pop1', 'pop2', 'pop3']
print('list2DeleteViaPop - %s' % list2DeleteViaPop)
list2DeleteViaPop.pop(1)
print("list2DeleteViaPop.pop(1) -> list2DeleteViaPop - %s" % list2DeleteViaPop)
list2DeleteViaPop.pop(1)
print("list2DeleteViaPop.pop(1) -> list2DeleteViaPop - %s" % list2DeleteViaPop)


# Delete - list.remove(value) -- value来删除
list2RemoveSpecificVlue = ['A', 'B', 'A', 'C']
print('list2RemoveSpecificVlue - %s' % list2RemoveSpecificVlue)
list2RemoveSpecificVlue.remove('A')
print("list2RemoveSpecificVlue.remove('A') -> list2RemoveSpecificVlue - %s" %
      list2RemoveSpecificVlue)
list2RemoveSpecificVlue.remove('A')
print("list2RemoveSpecificVlue.remove('A') -> list2RemoveSpecificVlue - %s" %
      list2RemoveSpecificVlue)


# Delete - list.clear() -- 清空列表的值且保留列表:
list2Clear = [1, 2, 3]
print('list2Clear - %s' % list2Clear)
list2Clear.clear()
print("list2Clear.clear() -> list2Clear - %s" % list2Clear)


# Delete - del list -- 删除整个列表:
list2BeDeleted = ['list2BeDeleted1', 'list2BeDeleted2']
print('list2BeDeleted - %s' % list2BeDeleted)
del list2BeDeleted


# type(list) -- Type of the list：
listA = [1]
print('type(listA) - %s' % type(listA))


# 多个list元素相互叠加操作 list1 + list2 -- 不改变numList1 numList2: numlist1 + numlist2
numlist1 = [1, 2, 3, 4, 5, 6, 7]
print('numlist1 - %s' % numlist1)
numlist2 = [8, 9, 10]
print('numlist2 - %s' % numlist2)
numlist3 = numlist1 + numlist2
print("numlist3 = numlist1 + numlist2 -> numlist3 - %s" % numlist3)
print('numlist1 - %s' % numlist1)
print('numlist2 - %s' % numlist2)


# 多个list元素相互叠加操作 - list1.extend(list2) -- 改变numList1 numList2: numlist1.extend(numlist2)
numlist1 = [1, 2, 3, 4, 5, 6, 7]
print('numlist1 - %s' % numlist1)
numlist2 = [8, 9, 1]
print('numlist2 - %s' % numlist2)
numlist1.extend(numlist2)
print("numlist1.extend(numlist2) -> numlist1 with numlist2 value appended - %s" % numlist1)
print('numlist2 - %s' % numlist2)
###################################################### 数据类型 list ######################################################
