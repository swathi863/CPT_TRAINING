'''
import time
print(time)
epoch=time.time()
print(epoch)
'''
'''
Epoch time (also called Unix time or POSIX time) in Python is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC (the Unix Epoch).
'''

#converting epoch time to readable format
'''
import time

epoch_time = 1720165800
readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))
print(readable_time)
'''
#convertinng date time to epoch
'''
import datetime

dt = datetime.datetime(2025, 7, 5, 12, 0, 0)  # Any datetime
epoch_time = dt.timestamp()
print(epoch_time)
'''