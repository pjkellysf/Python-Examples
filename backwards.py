#!/usr/local/bin/python3
# Patrick Kelly
# September 29, 2015
# Write a program that prints out its own command line arguments, but in reverse order.

# Note: The arguments passed in through the CLI (Command Line Interface) are stored in sys.argv.
# Assumption: The first item argument in sys.argv is the filename and should NOT be included in the output.

# Import the sys module
import sys

# Subtract one from the length of sys.argv to access the last index and store the result in the variable argumentIndex.
argumentIndex = len(sys.argv) - 1

# Iterate through sys.argv starting with the last argument at index argumentIndex.
for argument in sys.argv:
    # Exclude the filename which is the first argument in sys.argv at index 0.
    if argumentIndex > 0:
        # Print out the indexed argument from sys.argv
        print (sys.argv[argumentIndex])
        # Decrement argumentIndex to access the previous argument in the next loop
        argumentIndex -= 1
