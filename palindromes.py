#!/usr/local/bin/python3
# Patrick Kelly
# October 28, 2015

# A program which finds any palindromes over seven letters long in the dictionary
# /users/abrick/resources/american-english-insane

# Set the content of the dictionary file to a file handler.
fh = open('/users/abrick/resources/american-english-insane')
# Assign the minimum length of the palindrome to be found and initialize the count to zero.
minLetters = 7
count = 0

# Iterate through the contents.
for line in fh:
    # Strip out the line return and assign the result to a variable.
    word = line.strip()
    # Compare the forwards and backwards strings.
    #   AND
    # Compare the length of the word to the minimum length.
    if word == word[::-1] and (len(word) > minLetters):
        # If the word is a palindrome and meets the length requirement, increment the count and print the result.
        count += 1
        print('The word',word,'is a palindrome with more than',minLetters,'letters.')
        
# Print the total number of palindromes found in the dictionary that meet the requierements.
print('The dictionary contains',count,'palindromes with more than',minLetters,'letters.')
# Close the file handler.
fh.close()
