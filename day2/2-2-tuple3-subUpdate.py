# 元组不能更改（元素的存储空间不能改变），但是元组内部的列表内部的元素可以改变的
muti_tuple = (1, 3, 5, 7, 9, ["python", "java", "c++"])
print("multi_tuple - %s" % (muti_tuple,))
muti_tuple[-1][0] = "php"
muti_tuple[-1].append("go")
print("multi_tuple - %s" % (muti_tuple,))

''' 元组元素指针不可变的使用案例，付款，网络卡顿重复添加问题 '''
