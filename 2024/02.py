# Full instructions for this task can be found at: https://adventofcode.com/2024/day/2

# Part 1: Iterate through each report and verify whether the are safe
# Reports are only safe if:
#  1. All consecutive values either increase OR decrease
#  2. Two consecutive numbers have a difference between 1 and 3


safeCount = 0 # Count the number of safe reports

# Iterates through the entire report of values checking if 
# they're in ascending order.
# Returns 0 if the report is SAFE, returns 1 is the report is UNSAFE
def ascendOrder(report):
    for index in range(len(report)):
        try:
            # Convert the values used to integers (ensures math is correct)
            val1 = int(report[index])
            val2 = int(report[index+1])
            if val1 < val2:
                continue
            if val1 > val2:
                return 1
        except:
            break
    return 0

# Iterates through the entire report of values checking if 
# they're in descending order.
# Returns 0 if the report is SAFE, returns 1 is the report is UNSAFE
def descendOrder(report):
    for index in range(len(report)):
        try:
            # Convert the values used to integers (ensures math is correct)
            val1 = int(report[index])
            val2 = int(report[index+1])
            if val1 > val2:
                continue
            if val1 < val2:
                return 1
        except:
            break
    return 0

# Iterates through the entire report of values checking if
# the difference between each consecutive value is between 1 and 3
# Increments the safeCount if true, does nothing if not
def oneToThreeDifference(report):
    for index in range(len(report)):
        try:
            # Convert the values used to integers (ensures math is correct)
            val1 = int(report[index])
            val2 = int(report[index+1])
            checker = abs(val1 - val2)
            if 1 <= checker <= 3:
                continue
            else:
                return
        except:
            break

    global safeCount
    safeCount+=1

# Open the input file and read one line (report) at a time
# Check the first two values in the report:
#   if val1 < val2 then check that all values are in ascending order
#   if val1 > val2 then check that all values are in descendin order
# If that validation check succeeds, then continue checking if there
# is between a 1 and 3 difference between consecutive values
with open("2024/02-inputTEST.txt", "r") as inFile:
    line = inFile.readline()
    valList = line.split()

    try:
        index = 0
        # Convert the values used to integers (ensures math is correct)
        val1 = int(valList[index])
        val2 = int(valList[index+1])
        if val1 < val2:
            valid = ascendOrder(valList)
            if valid == 0:
                check = oneToThreeDifference(valList)
        if val1 > val2:
            valid = descendOrder(valList)
            if valid == 0:
                oneToThreeDifference(valList)
    except:
        print("done")

inFile.close()

print(safeCount)
# iterate through the list
#     flag for safe = 0
#     compare list[0] to list[1]
#         if 0 < 1 then check if list is in ascend order
#             if not, safe flag = 1, quit
#             if yes, check if each value is between 1-3 different
#                 if either fails safe flag = 1, quit
#         if 0 > 1 then check if list is in descend order
#             if not, safe flag = 1, quit
#             if yes, check if each value is between 1-3 different
#                 if either fails safe flag = 1, quit