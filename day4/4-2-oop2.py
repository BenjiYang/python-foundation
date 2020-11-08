# 类 模板


class People:
    # 对象可以强行增加类没有的属性 - 非常容易被增加属性对象，灵活性，但涉及安全问题
    # __slots__: 限制属性，对象不可另外增加其他属性
    __slots__ = {"name", "age", "weight"}

    # __init__: __特殊方法__，用于对象初始化：
    # self 相当于自身，java的this

    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight

    def work(self):
        print("%s正在努力工作" % self.name)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


# 基于类创建对象
p1 = People(name="Annie", age=25, weight=90)
# 类似java的toString()打印出所有对象属性
print(p1.get_name)
# print(p1.__dict__)

p2 = People(name="SlotCase", age=20, weight=80)
p2.newField = '2'
print(p2.__dict__)
