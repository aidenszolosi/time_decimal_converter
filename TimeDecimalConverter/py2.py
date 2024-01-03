import math
import re

def decToTime(time_decimal):
    time = time_decimal
    timeFloat = float(time)
    try: 
        decimalVal = re.findall(r'\.\d+', str(timeFloat))
        decimalVal = decimalVal[0]
    except Exception as e:
        print(f"There is likely no decimal number. Exception: {e}")

    HourNum = math.floor(timeFloat)
    if HourNum >= 12:
        isPM = True
    elif HourNum < 12:
        isPM = False
    else:
        print(f"Big fuckign error ")

    if HourNum == 0:
        isPM = False
        HourNum = 12
        print("Hour num is 0")

    #IF PM EXISTS
    if isPM:
        HourNum = HourNum - 12
        # print(f"{HourNum}PM")
        meridiem = "PM"
    elif not isPM:
        # print(f"{HourNum}AM")
        meridiem = "AM"


    mins = 60 * float(decimalVal)
    mins = round(mins)
    mins = int(mins)
    if mins == 60:
        mins = mins - 1
    if mins <= 9:
        mins = f"0{mins}"
    if HourNum == 0:
        HourNum = 12
    if mins:
        res = (f"{HourNum}:{mins}{meridiem}")
        return res



# timeInput = input(f"Enter the float time (0.0 - 23.99): ")

# print(decToTime(timeInput))