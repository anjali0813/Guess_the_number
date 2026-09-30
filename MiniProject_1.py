# GUESS THE NUMBER 

import random

target = random.randint(1, 100)

while True:
    userChoice  = input("Guess the number or Quit (Q) : ")
    if(userChoice == "Q" or "q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("SUCCESS. You guessed it right !!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess !!")
    else:
        print("Your number was too big. Take a smaller guess !!")

print("------GAME OVER-------")