# Datetime: it is a module that provides classes for manipulating dates and times in both simple and complex ways. It allows you to work with date and time objects, perform arithmetic operations on them, and format them in various ways.
import datetime

print(dir(datetime))
[
    "MAXYEAR",
    "MINYEAR",
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
    "date",
    "datetime",
    "datetime_CAPI",
    "sys",
    "time",
    "timedelta",
    "timezone",
    "tzinfo",
]

from datetime import datetime
now = datetime.now()
print(now)                      # the time when the code is executed
day = now.day                   # the current day of the month
month = now.month               # the current month
year = now.year                 # the current year
hour = now.hour                 # the current hour
minute = now.minute             # the current minute
second = now.second             # the current second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # formatting the date and time in a specific way

# Formatting date and time using strftime() method
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)     
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)   

# String to datetime conversion using strptime() method
from datetime import datetime
date_string = "2 September, 2026"
print("date_string =", date_string)     # date_string = 2, September, 2026
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2026-09-02 00:00:00

# Using date from datetime module
from datetime import date
d = date(2020, 1, 1) # create a date object of 1st January 2020
print(d)        # 2020-01-01
print('Current date:', d.today())    # 2026-09-02
# date object of today's date
today = date.today() 
print("Current year:", today.year)   # 2026
print("Current month:", today.month) # 9
print("Current day:", today.day)     # 2

# Objects to represent time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555

# Difference between two dates using:
from datetime import date, datetime
today = date(year=2026, month=9, day=2)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year: 
print('Time left for new year: ', time_left_for_newyear)  

t1 = datetime(year = 2026, month = 9, day = 2, hour = 0, minute = 0, second = 0)
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# Difference between two dates using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)