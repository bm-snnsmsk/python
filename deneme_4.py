
import datetime

t = '21 April 2019 hour 20:42:18'


dt = datetime.datetime.strptime(t, '%d %B %Y hour %H:%M:%S') 

print(dt)