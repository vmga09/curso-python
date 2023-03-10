
"""

Dia n16
"""

from datetime import datetime, date
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
# f'  format string with variable
print(f'{day}/{month}/{year}, {hour}:{minute}')

t = now.strftime("%Y-%m-%d %H:%M:%S")
print(t)

date_string = "5 December, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

d = date(2022, 1, 1)
print(d)
