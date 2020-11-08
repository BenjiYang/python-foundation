import pickle


def foo():
    print("foo")


# dumps - 序列化：对象转字节码
str_serialized = pickle.dumps(foo)
print(str_serialized)

# loads - 反序列化：字节码转对象
str_deserialized = pickle.loads(str_serialized)
print(str_deserialized)
# 反序列化后到变量（方法）可直接使用
str_deserialized()


# dump - 序列化：对象转文件
num_list = range(100)
print(num_list)
# 打开文件
my_file = open("num_lis.txt", "wb+")
# 操作写入内容到文件
ret_test = pickle.dump(num_list, my_file)
# 关闭文件
my_file.close()


# load - 反序列化：文件转对象
my_file = open("num_lis.txt", "rb+")
ret_num_list = pickle.load(my_file)
my_file.close()
print(ret_num_list)
