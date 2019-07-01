import datetime

sunday = 6
day = datetime.datetime.fromisoformat('1901-01-01')

count = 0
while True:
    date = str(day.date())
    day_number = int(date.split('-')[-1])

    if day_number == 1 and day.weekday() == 6:
        count += 1

    if date == '2000-12-31':
        break

    day += datetime.timedelta(1)

print(count) # 5270