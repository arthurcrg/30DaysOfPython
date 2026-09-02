import datetime

print(f'Right now it is {datetime.datetime.now()}')
print(f'The current date formatted is {datetime.datetime.now().strftime("%d/%m/%Y")}')

date_string = '2 September, 2026'
date_object = datetime.datetime.strptime(date_string, '%d %B, %Y')
print(f'The date object is {date_object}')

now = datetime.datetime.now()
new_year = datetime.datetime(year=now.year + 1, month=1, day=1)
time_until_new_year = new_year - now
print(f'Time until New Year: {time_until_new_year}')

last_century = datetime.datetime(year = 1970, month = 1, day = 1)
now = datetime.datetime.now()
time_since_last_century = now - last_century
print(f'Time since last century: {time_since_last_century}')
