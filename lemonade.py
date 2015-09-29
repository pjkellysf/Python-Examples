#CS131A Assignment 2 - Patrick Kelly
#A program which estimates the cost to prepare 100 servings of lemonade.
#Tools - python language, brackets for editing locally, hills.ccsf.edu for testing on server
#Resources - text input, text output, internet searches for recipes and prices of ingredients
#Kind of Lemonade - regular lemonade recipe from Google
#Adding a comment to test GitHub.

#Recipe for 5 servings of lemonade from google
#1 cup sugar
#6 lemons
#3 cups cold water

#!/usr/local/bin/python3
#Price of a lemon
lemonPrice = .50
#Total number of lemons in 100 servings
totalLemons = 120
#Price of a cup of sugar
sugarPrice = .21
#Total number of cups of sugar in 100 servings
totalCupsOfSugar = 20
#Price of a cup of water
waterPrice = 0
#Total number of cups of water in 100 servings
totalCupsOfWater = 60

#Function to determine cost of 100 servings of lemonade
def calculateCost():
     #calculate lemon cost
     lemonCost = lemonPrice * totalLemons
     #calculate sugar cost
     sugarCost = sugarPrice * totalCupsOfSugar
     #calculate water cost
     waterCost = waterPrice * totalCupsOfWater
     #calculate the total cost by adding the individual costs
     totalCost = lemonCost + sugarCost + waterCost
     return(totalCost)

#Run to function
finalTotal = calculateCost()
#Turn the result into a string
finalTotalString = str(finalTotal)
#Print out the result
print("Based on a cost of .50¢ per lemon, .21¢ per cup of sugar and free water...")
print("It costs $" + finalTotalString + "0" + " to make 100 servings of lemonade!")
