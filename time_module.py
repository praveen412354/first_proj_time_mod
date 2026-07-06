import time

print(time.time())
print(time.ctime())
current_date_time=time.localtime()
print(type(current_date_time))
print(current_date_time)

print(time.strftime('%Y-%m-%d %H:%M:%S'))



