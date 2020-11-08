# 普通装饰器
def decorate(func):
    def wrapper():
        print("decorate is running!")
        # not declaring func() - function skipped
        print("inner is running")
    return wrapper


@ decorate
def foo1():
    print("running foo1")


foo1()
