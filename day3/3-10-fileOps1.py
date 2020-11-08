f1 = open("1.txt", "w")
f1.write("line1\n")
f1.write("line2\n")
f1.write("line3\n")
f1.close()


f1 = open("1.txt", "r")
print(f1.read())
print(f1.readline())
print(f1.tell())  # tell() 当前下标
print(f1.seek(1))  # seek(index) 重置下标到index
print(f1.tell())
print(f1.readlines())  # readlines() - 读取所有行
f1.close

f1 = open("1.txt", "w")
f1.write("new line1\n")  # write(str) - 覆盖
f1.close

f1 = open("1.txt", "rb+")
print(f1.readlines)
f1.close
