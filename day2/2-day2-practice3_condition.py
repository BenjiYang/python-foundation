''' 练习3 - 
输入你的年龄，
>60, 返回老年人；
30-60（包括60）为中年人；
18-30（包括18与30）成年人；
小于18，未成年人
'''
age = int(input('请输入你的年龄: '))
if age > 60:
    print("老年人")
elif age > 30 and age <= 60:
    print("中年人")
elif age >= 18 and age <= 30:
    print("成年人")
elif age < 18:
    print("未成年人")
else:
    print("输入有误！！")
18
