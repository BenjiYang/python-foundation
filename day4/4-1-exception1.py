# 异常处理容易抛出问题的代码，做处理，如：文件操作，网络连接等


# 被动抛出异常 -- try except else finally
try:
    f = open("./demo.txt", "r", encoding="utf-8")
    print(f.read(10))
    f.close()
except Exception as e:
    print(e)
else:
    print("程序正常执行")
finally:
    print("无论是否异常，finally都执行，如用于资源管道关闭等")

print("END!")


# 主动抛出异常 -- raise Exception()
num = input("请输入一个整数：")
if num.isdigit():
    print(num)
else:
    raise Exception("你输入的值非整数，请重新输入！")
