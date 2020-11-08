# 案例1：设计一个时钟类（时分秒），tick()方法被调用一次，秒钟就+1

# 案例2：设计一个日历类（年月日），next_day()方法被调用一次，天就+1

# 案例3: 涉及一个时钟日历类（年月日时分秒），tick()方法被调用一次，秒钟就+1，能够联动日历更新

# 1.
# clock = Clock(23, 59, 59)
# clock.tick()
# 00.00.00

# 2.
# calendar = Calendar(2008, 12, 30)
# calendar.next_day()
# 2009-01-01

# 3. clock_calendar = ClockCalendar(2020, 12, 30, 23, 59, 59)
# clock_calendar.tick()
# 2021-01-01 00:00:00


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # __str__: 在调用print函数打印对象时，会调用__str__ 方法

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)

    def tick(self):
        if self.second == 59:
            if self.minute == 59:
                if self.hour == 23:
                    self.hour = 00
                    self.minute = 00
                    self.second = 00
                else:
                    self.hour += 1
                    self.minute = 1
            else:
                self.minute += 1
        else:
            self.second += 1


clock = Clock(23, 59, 59)
print(clock)  # 默认调用__str__方法
clock.tick()
print(clock)


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # __str__: 在调用print函数打印对象时，会调用__str__ 方法

    def __str__(self):
        return "%04d-%02d-%02d" % (self.year, self.month, self.day)

    def next_day(self):
        if self.day == 30:
            if self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1


calendar = Calendar(2008, 12, 30)
print(calendar)
calendar.next_day()
print(calendar)


# 继承
class ClockCalendar(Clock, Calendar):
    def __init__(self, year, month, day, hour, minute, second):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, year, month, day)

    def __str__(self):
        return Calendar.__str__(self) + " " + Clock.__str__(self)

    def tick(self):
        Clock.tick(self)
        if self.hour == 0 and self.minute == 0 and self.second == 0:
            Calendar.next_day(self)


clock_calendar = ClockCalendar(2009, 12, 30, 23, 59, 59)
print(clock_calendar)
clock_calendar.tick()
print(clock_calendar)
