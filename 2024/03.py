#  Full instructions can be found at: https://adventofcode.com/2024/day/3

import re
import operator

# PART 1: Find all occurrences of multiplication functions in the puzzle input, execute them and all their products together

matchList = []                  # Create an empty list to store regex matches
newList = []                    # Create an empty list of multiplication functions to execute
target = "mul"
replacement = "operator.mul"    # Replace occurrences of "mul" with "operator.mul" in regex matches
total = 0                       # Running sum of multiplication functions

# Use a regular expression to look for all occurrences of legitimate multiplication instructions
# from the puzzle input
pattern = r"mul\(\d{,3},\d{,3}\)"

# Open the puzzle input as a file, reading one line at a time and do:
#   1. Find all occurrences of legitimate multiplication functions mul(XX,XX)
#   2. Create a new list of multiplication functions operator.mul(XX,XX)
#   3. Execute the multiplication functions and add each product to the running total
with open("2024/03-input.txt", "r") as inFile:
    for line in inFile:
        # Find all occurrences of legit mult functions
        matchList = re.findall(pattern, line) 

        # Create a new list of multiplications, replacing "mul" with "operator.mul"
        newList = [item.replace(target, replacement) for item in matchList] 
        
        #Execute the multiplications and calculate a running total
        for i in range(len(newList)):
            total = total + eval(newList[i])

# Print the total and close the input file
print(f"Total of ALL multiplications is: {total}")
inFile.close()

# Part 2: Find all occurrences of multiplication functions in the puzzle input,
# but only execute those who either come before a don't() function or are enabled by a do() function

