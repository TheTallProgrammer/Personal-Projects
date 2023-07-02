# Logan Falkenberg

# 1 GB = 1000 MB

# Import Modules
import math

# ---------------------------------------------------------------------------------------
# Enter the average number of GB remaining
print("")
gbRemainingInput = float(input("Enter the average number of GB remaining: "))
gbRemaining = float(gbRemainingInput)

# Enter the average amount of MB/s
print("")
mbPSInput = float(input("Enter the average amount of MB/s: "))
mbPS = float(mbPSInput)

# ---------------------------------------------------------------------------------------


# Make a variable for the outcome of converting it to GB
mbConversion = float(mbPS * 0.001)

# Getting the seconds by dividing GB by MB/s
secondsLeft = float(gbRemaining / mbConversion)

# Get's remaining minutes by dividing the seconds left by 60
minutesLeft = float(secondsLeft / 60)

# Seperates the minutes and seconds (seconds, minutes)
secondsCommaMinutes = math.modf(minutesLeft)

# Get's only the seconds at index ([0],1)
secondsLeftOnly = float(secondsCommaMinutes[0])

# Get's only the minutes at index (0,[1])
minutesLeftOnly = int(secondsCommaMinutes[1])

# Converts the seconds from the remaining seconds into the actual seconds remaining
actualSecondsRemaining = secondsLeftOnly * 60

# Pulls out any hours out of the minutes by dividing minutes by 60
hoursLeft = int(minutesLeftOnly / 60)

# Print final result of remaining time
if minutesLeftOnly >= 60:
    minutesLeftOnly = minutesLeftOnly - (hoursLeft * 60)
    print("---------------------------------------------------------------------------")
    print("")
    print("Hours Remaining: " + str(hoursLeft))
    print("Minutes Remaining: " + str(minutesLeftOnly))
    print("Seconds Remaining: " + str(actualSecondsRemaining))
    print("")
    print("---------------------------------------------------------------------------")
else:
    print("---------------------------------------------------------------------------")
    print("")
    print("Minutes Remaining: " + str(minutesLeftOnly))
    print("Seconds Remaining: " + str(actualSecondsRemaining))
    print("")
    print("---------------------------------------------------------------------------")

endGameInput = str(input("Press ENTER to close"))
endGame = str(endGameInput)

