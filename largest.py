#!/usr/local/bin/python3
# Submit as “largest” a program which identifes the single largest number, written in digits, occurring in the Urantia Book, as found in /users/abrick/resources/urantia . Hint: the number is in the trillions.
# Patrick Kelly
# CS131A
# Fall 2015

# Import the re module   
import re
# Open the text file and assign it to a file handler
fh = open("/users/abrick/resources/urantia", "r")
# Initialize a list to hold the numbers found in the search
largestList = []

for line in fh:
    # Test for lines that have digits
    if re.search(r'\d', line):
        # Remove the line breaks in the matching lines
        line = line.strip()
        # Seperate the elements in the matching line along a space
        words = line.split(' ')
        # Iterate though the words and remove characters that confuse the numbers
        for word in words:
            # Remove periods
            word = word.strip('.')
            # Remove semi-colons
            word = word.strip(';')
            # Remove commas and rejoin so its a recognizable number for xxx, patterns
            word = word.split(",")
            word = ''.join(word)
            # Test the results and turn words that can be integers into integers
            if re.search(r'^\d.*\d$', word) and "-" not in word and ":" not in word:
                num = int(word)
                # Add the integer to the list
                largestList.append(num)
                
# Find the largest integer in largestList and print out the result
largest = max(largestList)
print(largest,"is the largest number in The Urantia Book.")
