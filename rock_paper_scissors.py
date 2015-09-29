#!/usr/local/bin/python3
# Patrick Kelly
# Rock Paper Scissors Game
# September 27, 2015
# This program simulates the popular Rock - Paper - Scissors childhood game.
# The user will be prompted to enter either r, p, or s.
# The program will generate a random choice of either r, p, or s.
# Either a tie or a winner will be declared.
# A win will award the winning player with one point for that round.
# The game is over when the first player reaches 3 points.

# import modules
# Used to generate a random number between 0 and 2 to choose rock paper or scissors from a list
import random

#initialize variables
choiceOne = ""
choiceTwo = ""
choiceList = ["r", "p", "s"]
choiceNameList = ["Rock", "Paper", "Scissors"]  #not used yet

# The following functions will be explored and used as needed:
# printGameIntro()          // Welcomes the player, explains the game
# startNewGame()            // Clears any variables used to score the game
# startNewRound()           // Clears any variables used to score a round 
# askUserChoice()           // Asks for user input "r", "p", or "s"
# validateUserChoice()      // Determines if the user has used a correct input variable "r", "p", or "s"
# generateRandomChoice()    // Generates a random choice "r", "p" or "s"
# determineWinner()         // Determines tie or win, awards points and gives user feedback in print form
# updateScore()             // Updates the totals for both players and determines if the game is over
# gameOver()                // Informs the user who won and asks if they want to play again or exit
# exitProgram()             // Exits the python program back to the Unix prompt

#Function definitions (Had to refactor this code using parameters because variables were out of scope in functions...)

# Asks for user input "r", "p", or "s" for Player One
def askUserChoice():
    c1 = input("Enter 'r', 'p', or 's' : ")
    return(c1)

# Generates a random choice "r", "p" or "s" for Player Two
def generateRandomChoice():
    ranNum = random.randint(0, 2)
    c2 = choiceList[ranNum]
    return(c2)

# Determines tie or winner and gives user feedback in print statements
def determineWinner(c1, c2):
    print("Player One Chose:",c1)
    print("Player Two Chose:",c2)
    if (c1 == c2):
        print("This round is a TIE.")
        startNewRound()
    else:
        print("This round is NOT a TIE.")
        # Rock Paper
        if c1 == "r" and c2 == "p":
            print("Player Two Wins! Paper Covers Rock!")
        # Rock Scissors
        if c1 == "r" and c2 == "s":
            print("Player Two Wins! Rock Smashes Scissors!")
        # Paper Scissors
        if c1 == "p" and c2 == "s":
            print("Player Two Wins! Scissors Cut Paper!")
        # Paper Rock
        if c1 == "p" and c2 == "r":
            print("Player One Wins! Paper Covers Rock!")
        # Scissors Rock
        if c1 == "s" and c2 == "r":
            print("Player Two Wins! Rock Smashes Scissors!")
        # Scissors Paper
        if c1 == "s" and c2 == "p":
            print("Player One Wins! Scissors Cut Paper!")
    #startNewRound() Need to add a way to exit the program
        
# Welcomes the player
def printGameIntro():
    print("Welcome to Rock - Paper - Scissors !")
        
# Start a round
def startNewRound():
    choiceOne = askUserChoice()
    choiceTwo = generateRandomChoice()
    determineWinner(choiceOne, choiceTwo)
    
# Finally call these functions to run the game
printGameIntro()
startNewRound()
