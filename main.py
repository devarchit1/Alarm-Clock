from datetime import datetime   
from playsound import playsound
import time

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")

# create new datetime object from input string
alarm_time_dt = datetime.strptime(alarm_time, "%I:%M:%S%p")

while True:
    now = datetime.now()

    # check if current datetime equals alarm datetime
    if now == alarm_time_dt:
        print("Wake Up!")
        playsound('audio.mp3')
        break

    # to lower cpu usage
    time.sleep(1)
