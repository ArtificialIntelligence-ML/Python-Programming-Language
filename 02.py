from datetime import datetime
#import datetime
import time
import random

 
odds = [1,  3,  5,  7,  9,  11, 13, 15, 17, 19, 21, 23, 25,
        27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
        53, 55, 57, 59]

right_this_minute = datetime.today().minute
#right_this_minute = datetime.datetime.today().minute

# time_now = datetime.today()
# right_this_minute = time_now.minute

for i in range(4):
    if right_this_minute in odds:
        print("Odd minute")
    else:
        print("Not an odd minute")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)

