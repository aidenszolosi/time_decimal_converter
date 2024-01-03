import random
from py2 import decToTime
##time to float and back experiment

timeList = [
    "08:00AM",
    "09:30AM",
    "11:00AM",
    "12:30PM", 
    "02:00PM", 
    "03:30PM", 
    "05:00PM", 
    "06:30PM", 
    "08:00PM"
    ]

listLength = len(timeList) - 1
randomSel = random.randint(0,listLength)

randTime = timeList[randomSel]
# randTime = "12:30PM"
# print(randTime)

def TimeToDec(time):
    if time.endswith("AM"):
        isPM = False
    elif time.endswith("PM"):
        isPM = True

    hour = time[0:2]
    if hour.startswith("0"):
        hour = int(hour)

    mins = time[3:5]

    if isPM:
        meridiem = "PM"
    elif not isPM:
        meridiem = "AM" 

    # print(f"{hour}:{mins}{meridiem}")


    if meridiem == "PM" and float(hour) != 12:
        hour = float(hour)+float(12)
    elif meridiem == "AM":
        hour= float(hour)

    decimal = float(mins)/60

    floatresult = float(decimal) + float(hour)
    # print(floatresult)
    # print(decToTime(floatresult))
    return floatresult

TimeToDec(time=randTime)   










