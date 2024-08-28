'''
from datetime import date

# date(year, month, date)
d = date(2000, 12, 5)
# print(d)
today = date.today()
print(today, type(today))
print(today.year, today.day, today.month)
string_date = date.isoformat(today)
print(string_date, type(string_date))
'''

'''
from datetime import time

#time(hour, mins, seconds)
t = time(8, 50, 30)
print(t)
print(t.hour, t.minute, t.second)
'''
'''
from datetime import datetime

# datetime(year, month, date, hour, min, sec)
dt = datetime(2020, 12, 12, 13, 15)
print(dt.year)
print(dt.minute)
curr_time = datetime.now()
print(curr_time)
'''

import calendar
year = 2024
month = 8
day = 25
# print(calendar.month(year, month))
# print(calendar.isleap(year))
# Monday -> 0, 1, 2, 3, 4 - Sunday
# print(calendar.weekday(year, month, day))
print(calendar.calendar(year))