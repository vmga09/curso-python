
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

today = date(2022, 2, 15)
new_year = date(2023, 3, 13)
time_left_for_newyear = str(
    (new_year - today)).split(',')[0].split(' ')[0]  # Solo en dias
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)


# 💻 Exercises: Day 16
# Get the current day, month, year, hour, minute and timestamp from datetime module
fecha = datetime.now()
print(fecha)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(fecha.strftime("%m/%d/%Y %H:%M:%S"))
#     Today is 5 December, 2019. Change this time string to time.
fecha_string = "5, December, 2019"
fecha_time = datetime.strptime(fecha_string, "%d, %B, %Y")
print(fecha_time)
#     Calculate the time difference between now and new year.
diff_new_year = date(2024, 1, 1) - date(fecha.year, fecha.month, fecha.day)
print(diff_new_year)
#     Calculate the time difference between 1 January 1970 and now.
diff_new_year = date(fecha.year, fecha.month, fecha.day) - date(1970, 1, 1)

print(diff_new_year)
#     Think, what can you use the datetime module for ? Examples:
#     Time series analysis
#     To get a timestamp of any activities in an application
#     Adding posts on a blog
#     🎉 CONGRATULATIONS ! 🎉
