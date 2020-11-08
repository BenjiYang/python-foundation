############# 装饰器，类似于java的注解 #############
# 装饰器练习：给函数加统计运行时间功能
import time


def calculate_time_elapse(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("开始计时 %s" % start_time)
        # 运行 function
        func(*args, **kwargs)
        end_time = time.time()
        print("结束计时 %s" % end_time)
        print('%s 函数运行了：%f秒' %
              (func.__name__, end_time - start_time))
    return wrapper


# 方法名上添加 @装饰器名
@ calculate_time_elapse
def foo1():
    print("foo1")


def foo2():
    print("foo2")


foo1()
foo2()
############# 装饰器，类似于java的注解 #############
