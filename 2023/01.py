# Full instructions for this task can be found at: https://adventofcode.com/2023/day/1

# Part 1: Extract the first and last digits in each line of the input, 
# combine them into a 2 digit number and add them to a running total

digit1 = ""     # First digit extracted from input
digit2 = ""     # Second digit extracted from input
total = 0       # Total of all extracted values

# Open the text file containing all input strings
with open("2023/01-input.txt", "r") as inFile:
    for line in inFile:
        # Strip any trailing newline characters
        clean = line.strip()

        # Find the first digit inside the string: loop through the characters from the start
        # and break when a digit is found
        for i in clean:
            if i.isdigit():
                digit1 = i
                break

        # Find the last digit inside the string: loop through the characters from the end
        # and break when a digit is found
        reverse = str(clean[::-1]) # Reverse the input string from the file
        for i in reverse:
            if i.isdigit():
                digit2 = i
                break

        # Combine the two extracted digits to form a two digit number and convert this to an int
        number = digit1 + digit2
        intNum = int(number)

        # Calculate the total of all extracted numbers
        total += intNum

# Print the total and close the input file
print(f"total is {total}")
inFile.close()

# PART 2: Reexamine the input, and extract digits that are spelled out rather than numerically shown