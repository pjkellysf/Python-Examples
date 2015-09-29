#!/usr/local/bin/python3
# Patrick Kelly
# Calculate the average name length and longest name in the math and sys python modules
# Part A
# Are the names in the math module or the sys module longer on average
# Part B
# Which is the single longest name overall

#import libraries
import math
import sys

#initialize variables
mathList = dir(math)
mathListName = "math"
sysList = dir(sys)
sysListName ="sys"

#function to calculate average name length and longest name in the specified module
def calculateAverage(whichList, whichName):
    count = 0
    longestLength = 0
    longestName = ""
    for names in whichList:
        count += len(names)
        if len(names) > longestLength:
            longestLength = len(names)
            longestName = names
    average = count/len(whichList)
    print("The average length of names in the",whichName,"module is",int(average),"characters.")
    print("The longest name in the",whichName,"module contains",longestLength,"characters.")
    print("The longest name in the",whichName,"module is \'",longestName,"\'.")
    print("")
    
#call the function with the initialized variables as parameters
calculateAverage(mathList, mathListName)
calculateAverage(sysList, sysListName)
