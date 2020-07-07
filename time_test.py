import time
now = time.localtime()
time_info = "%04d/%02d/%02d %02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
print(time_info)
