#!/usr/local/bin/python3
# Error handling exercise peer to peer coding with Paul Clifford
import sys
from sys import argv

fileList = []

# Catch error for the correct number of arguments
try:
    test = argv[2]
except IndexError:
    print("Not enough arguments.")
    sys.exit()

# Test if user has included -v (exclude results) in the argument list
if argv[1] == '-v':
    n = 3
else:
    n = 2

# loop through files in argument list and catch errors for FileNotFound and PermissionError
def grep(n):
    for item in argv[n::]:
        filename =  item
        try:
            fh = open(filename)
            fileList.append(filename)       
        except FileNotFoundError:
            print(filename,"not found!")
        except PermissionError:
            print("You don't have permission to open", filename)
        fh.close()

def outputline(n):
    lineCounter = 0
    for file in fileList:
        fh = open(file)
        for line in fh:
            lineCounter += 1
            line = line.strip()
            if n == 2:
                if argv[1] in line:
                    seq = (file, str(lineCounter) ,line)
                    outputLine = ':'.join(seq)    
                    print(outputLine)
            else:
                if argv[2] not in line:
                    seq = (file, str(lineCounter), line)
                    outputLine = ':'.join(seq)
                    print(outputLine)
                    
# Call the functions
grep(n)
outputline(n)
