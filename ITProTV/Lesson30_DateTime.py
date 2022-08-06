from datetime import datetime, timedelta

today = datetime.now()
print(today.year)
print(today.month)
print(today.day)
first_of_the_year = datetime(2022, 1,1)
how_many_days = today -first_of_the_year
print(how_many_days)
day_increment = timedelta(days=1)
tomorrow = today + day_increment
print(tomorrow)
print(tomorrow.day)
print(tomorrow.hour)