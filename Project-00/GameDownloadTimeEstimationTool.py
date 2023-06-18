import math

def get_input(prompt):
    print()
    return float(input(prompt))

# Getting Inputs
gb_remaining = get_input("Enter the average number of GB remaining: ")
mbps = get_input("Enter the average amount of MB/s: ")

# Conversion MB/s to GB/s
gbps = mbps / 1000

# Time calculation
seconds_left = gb_remaining / gbps
minutes_left = seconds_left / 60
minutes_left_int, seconds_fraction = math.modf(minutes_left)
seconds_left_only = seconds_fraction * 60
hours_left = minutes_left_int // 60

# Prints remaining time
print("---------------------------------------------------------------------------\n")
if minutes_left_int >= 60:
    minutes_left_int -= hours_left * 60
    print(f"Hours Remaining: {int(hours_left)}")
print(f"Minutes Remaining: {int(minutes_left_int)}")
print(f"Seconds Remaining: {int(seconds_left_only)}\n")
print("---------------------------------------------------------------------------")

input("Press ENTER to close")
