# Full instructions for this task can be found at: https://adventofcode.com/2024/day/1

# PART 1: Find the distance between all pairs in the eventual sorted lists of input given

leftCol=[]        # Values of the left column of input
rightCol=[]       # Values of the right column of input
leftVal = 0       # Extracts the left column value from the input file
rightVal = 0      # Extracts the right column value from the input file
sortedLeft=[]     # Values of the left column of sorted input
sortedRight=[]    # Values of the right column of sorted input
dist = 0          # Distance between a single pair of values
totalDistance = 0 # Distance between all pairs of values

# This function accepts two values (left and right columns of input),
# and returns the distance between the numberical values
def findDistance(left, right):
    if left > right:
        return (left-right)
    else:
        return (right-left)

# Open our input file and extract the left and right column values (location IDs)
# Save them in their own lists leftCol and rightCol
with open("2024/01-input.txt", "r") as inFile:
    for item in inFile:

        # Split each line into left and right columns, append
        # Extracted values to the left & right lists respectively
        leftVal, rightVal = item.split()
        leftCol.append(int(leftVal))
        rightCol.append(int(rightVal))

inFile.close()

# Sort both the left and right columns based on the values of location IDs
sortedLeft=sorted(leftCol)
sortedRight=sorted(rightCol)

# Now that the columns are sorted, we need to find the distance between the pairs
# and add the distance between each pair to the total distance between all pairs
for index in range(len(leftCol)):
    dist=findDistance(sortedLeft[index],sortedRight[index])
    totalDistance = totalDistance+dist

print(totalDistance)

# PART 2: Find the similarity score between the two sorted lists of input

count = 0           # Counts how many times a value from the sortedLeft col is found in sortedRight
similarity = 0      # Similarity score for a single value
totalSimularity = 0 # Total simularity score for the full list of values

# Iterate through the list of values in the sortedLeft list
# If the value at that index matches a value in the sortedRight list, increment the counter
# Calculate the similarity score for each value and add it to the totalSimilarity score
for indexL in range(len(sortedLeft)):
    # Reset the counter for each value in the list
    count = 0
    for indexR in range(len(sortedRight)):
        if sortedLeft[indexL] == sortedRight[indexR]:
            count+=1
            
    similarity = (sortedLeft[indexL]*count)
    totalSimularity = totalSimularity+similarity

print(totalSimularity)

    