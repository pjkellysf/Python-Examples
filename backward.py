#!/usr/local/bin/python3
# Revised version
# Write a program that prints out its own command line arguments, but in reverse order.
# Note: The arguments passed in through the CLI (Command Line Interface) are stored in sys.argv.
# Assumption: The first argument in sys.argv is the filename and should NOT be included in the output.

# Import the sys module
import sys

# Iterate through sys.argv backwards and print out the results excluding the filename.
for arg in (sys.argv)[:0:-1]:
    print(arg)
