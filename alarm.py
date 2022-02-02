# Python 3
#alarm

import datetime
import time
from youtube_player import main

alarmH = int(input("Please enter hour for alarm "))
alarmM = int(input("Please enter minute/s for alarm "))
amPm = str.lower(input("am or pm?"))

if (alarmH <= 12 and alarmM < 60) and (amPm == "am" or amPm == "pm"):
    print("Alarm is set for", alarmH, ":", alarmM, amPm)

else:
    print("Wrong Input")

if amPm =="pm":
    alarmH = alarmH + 12

while True:
    if (alarmH == datetime.datetime.now().hour
            and alarmM == datetime.datetime.now().minute):
        print("Time to wake up!")
        # function call youtube player
        main()
        break

    else:
        time.sleep(1)
