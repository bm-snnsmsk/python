# import datetime 
from datetime import datetime
from datetime import timedelta

# result = dir(datetime)
# result = dir(datetime.datetime)
# result = dir(datetime.time)
# result = dir(datetime.date)

# result = datetime.now()  # = datetime.now()
# result = datetime.now().year
# result = datetime.now().month
# result = datetime.now().day
# result = datetime.now().hour
# result = datetime.now().minute
# result = datetime.now().second

# # https://www.w3schools.com/python/python_datetime.asp
# result = datetime.ctime(datetime.now())
# result = datetime.strftime(datetime.now(), '%Y')  # 2024
# result = datetime.strftime(datetime.now(), '%X')  # 202:36:16
# result = datetime.strftime(datetime.now(), '%d')  # 14
# result = datetime.strftime(datetime.now(), '%A')  # Saturday
# result = datetime.strftime(datetime.now(), '%B')  # September
# result = datetime.strftime(datetime.now(), '%Y %B %A')  # 2024 September Saturday

t = '21 April 2019 hour 20:42:18'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S') # 2019-04-21 20:42:18
result = dt.year

birthday = datetime(1985,1,1) # 1985-01-01 00:00:00





print(result)
print(birthday)
print(datetime.timestamp(birthday))
print(datetime.timestamp(datetime.now()))   ## saniye
print(datetime.fromtimestamp(datetime.timestamp(birthday)))
print(datetime.fromtimestamp(0))   # 1970-01-01 03:00:00

result = datetime.now() - birthday

print(result)   # 14501 days, 21:06:38.371969        timedelta
print(result.days)   # 14501
print(result.seconds)   # 75998
print(result.microseconds)   # 371969

print(datetime.now() + timedelta(days=10)) # 2024-09-24 21:06:38.372850
print(datetime.now() + timedelta(days=10, minutes=100)) # 2024-09-24 22:46:38.372850
print(datetime.now() - timedelta(days=10, minutes=100)) # 2024-09-04 19:26:38.372850
