# 作业1 - 茅台（800.0512）买2手，五粮液（80.5076）买7手。需要总资金多少？（保留小数位后两位，字符串打印格式：一共需要xxxx.xx元）
maoTai = 800.0512
wuliangye = 80.5076
total = (maoTai * 200) + (wuliangye * 700)
print("一共需要%.02f元" % total)

# 作业2 - 手机号码 135-1234-5678 格式
phoneNum = "13512345678"
phoneNum[:3]
phoneNum[3:7]
phoneNum[7:11]
if (len(phoneNum) == 11 and phoneNum.isdigit):
    # print("%s-%s-%s" % (phoneNum[:3], phoneNum[3:7], phoneNum[7:11]))
    print("-".join([phoneNum[:3], phoneNum[3:7], phoneNum[7:11]]))
else:
    print("Phone number format is incorrect!")
