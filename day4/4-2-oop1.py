"""
Benji:pythonTraining WenjieYang$ ipython
Python 2.7.17 (default, Dec 23 2019, 21:25:33) 
Type "copyright", "credits" or "license" for more information.

IPython 5.10.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

In [2]: 
"""

# 类 模板


class People:
    # __init__: __特殊方法__，用于对象初始化：
    # self 相当于自身，java的this
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def work(self):
        print("%s正在努力工作" % self.name)


# 基于类创建对象
p1 = People(name="Annie", age=25, weight=90)
print(p1.name)
print(p1.age)
print(p1.weight)
# 类似java的toString()打印出所有对象属性
print(p1.__dict__)
p1.work()
