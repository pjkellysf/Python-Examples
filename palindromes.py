#!/usr/local/bin/python3
# Patrick Kelly
# CS131A
# October 28, 2015

#A program which finds any palindromes over seven letters long in the dictionary /users/abrick/resources/american-english-insane

# Set the content of the file to a variable.
wrapper = open('/users/abrick/resources/american-english-insane')
# Assign the minimum length of the palindrome to be found.
minLetters = 7

# Iterate through the contents
for line in wrapper:
    # Strip out the line return and assign the result to a variable
    word = line.strip()
    # Compare the forwards and backwards strings
    #   AND
    # Compare the length to the minimum length
    if word == word[::-1] and (len(word) > minLetters):
        #Print out the result
        print('The word',word,'is a palindrome with more than',minLetters,'letters.')
        
wrapper.close()
