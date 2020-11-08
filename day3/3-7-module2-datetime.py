import datetime

now_time = datetime.datetime.now()
print(type(now_time))
print(now_time)
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

three_day_later = datetime.datetime.now() + datetime.timedelta(days=30,
                                                               hours=3, minutes=10)
print(three_day_later)

# 转换类型 str -> datetime
