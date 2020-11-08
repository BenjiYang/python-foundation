str1 = "hello world!"
# 计算出现多少次数
str1.count("l")

# 判断是否以字符串结尾
str1.endswith("!")

# 寻找第一个字符串出现在哪个位置，从0开始
str1.find("l")

# 覆盖
str1.replace("hello", "Hello")

# 拆分
str1.split(" ")
str1.upperCase()

# 大小写转换
str1.upper()
str1.lower()

# 字符串截取
str2 = "0123456789"
# 截取最后3个字符
str2[-3:]
# 前三位 - 0,1,2 - 不包含后面 str2[3]的值
str2[:3]

# [start:stop:step]
# 多隔位切片 - 隔两位切分
str2[::2]
# 多隔位切片(反向输出) - 隔两位切分
str2[::-2]
