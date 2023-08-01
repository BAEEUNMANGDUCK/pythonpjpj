import datetime as dt


# 현재 시각
now = dt.datetime.now()
year = now.year
print(now)
print(type(now))
print(type(year))
print(year)

day_of_week = now.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=1995, month=9, day=7, hour=4)
print(date_of_birth)


