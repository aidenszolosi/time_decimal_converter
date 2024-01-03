from main import TimeToDec
from py2 import decToTime
tryAgain = True
print(
    f"Welcome to the time-decimal converter."
    f"\nPlease select an option."
    f"\n1. Time to Decimal"
    f"\n2. Decimal to Time"
)
userChoice = input("Select a number: ")
if userChoice == "1":
    timeInput = input(f"Enter Time: ")

    if not timeInput.startswith("0"):
        timeInput = f"0{timeInput}"

    DecimalResult = TimeToDec(timeInput)

    print(f"TIME TO DECIMAL: {DecimalResult}")
elif userChoice == "2":
    while tryAgain == True:
        decInput = input(f"Enter Decimal: ")
        if float(decInput) >= 24:
            print(f"UNEXPECTED NUMBER.")
            tryAgain = True
        else:
            tryAgain = False
            DecResult = decToTime(decInput)
            print(f"DECIMAL TO TIME: {DecResult}")

