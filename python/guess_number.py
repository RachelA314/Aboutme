# imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
#For Testing: print(aRandomNumber)
limit = 0
while limit < 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    limit += 1
    if not guess.isnumeric(): #check if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess)# converts a string to an integer
    if (limit == 3):
        print("No more guesses")
        break



    if (guess > aRandomNumber):
        print("Guess lower!")


    elif (guess < aRandomNumber):
        print("Guess higher!")


    else:
        print("You guessed the correct number!")
        break

    
