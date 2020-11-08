
# 元组解包
muti_tuple2 = (2, 4, "str", ("A", "B", "c"), ['a', 'b', 'c'])
''' 拆分（正则表达）定义多个变量来映射元组tuple的元素多个值 '''
myNum, *_, myList = muti_tuple2
print(myNum)
print(myList)
# 练习
people_tuple = ('Tom', 175, 22, [65, 77, 88, 99], 'guangzhou')
people_name, *_, [_, people_chineseScore, *_], people_city = people_tuple
print("%s's Chinese score is %s, and living in %s city" %
      (people_name, people_chineseScore, people_city))
