
''' 练习2 - [{'name': 'alice', 'age': 18, 'gender': 0}, {'name': 'tom', 'age': 48, 'gender': 0}, {'name': 'jim', 'age': 58, 'gender': 1}, {'name': 'evan', 'age': 48, 'gender': 1}]
对个人信息列表按年龄排序
ref: https://web.archive.org/web/20150222160237/stygianvision.net/updates/python-sort-list-object-dictionary-multiple-key/
'''
from operator import itemgetter

alice = {'name': 'alice', 'age': 18, 'gender': 0}
tom = {'name': 'tom', 'age': 48, 'gender': 1}
jim = {'name': 'jim', 'age': 58, 'gender': 1}
evan = {'name': 'evan', 'age': 48, 'gender': 0}
people_list = [alice, tom, jim, evan]


################################################# 单个元素排序 #################################################
# 单个元素排序方式1 with itemgetter() -- sorted(people_list, key=itemgetter('age'))
print('people_list \n %s' % people_list)
mylist = sorted(people_list, key=itemgetter('age'))
print(mylist)

# 单个元素排序方式2 lambda - sorted(people_list, key=lambda k: k['age'])
# 推荐方式 （/）
mylist = sorted(people_list, key=lambda k: k['age'])
print(mylist)

# 逆序使用
# 推荐方式 （/）
mylist = sorted(people_list, key=lambda k: -k['age'])
print(mylist)
################################################# 单个元素排序 #################################################


################################################# 多个元素排序 #################################################
# Sort by multiple keys - case sensitive
mylist = sorted(people_list, key=itemgetter('age', 'gender'))
print(mylist)

# Sort name alphabetically and age in descending order
# 推荐方式 （/）
mylist = sorted(people_list, key=lambda k: (k['name'].lower(), -k['age']))
print(mylist)
################################################# 多个元素排序 #################################################
