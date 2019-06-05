#game.py

import random

print("Rock, Paper, Scissors, Shoot!")  

#capture input

user_choice = input("Please chose one of the following options: 'rock', 'paper' or 'scissors' (without the quotes):")

print("----------")
print("User chose:",user_choice)


#validate input

if user_choice not in["rock","paper","scissors"]:     
    print("Invalid Selection Please Try Again")
    exit()

#generate computer selection
print("Generating...") 

computer_choice = random.choice(["rock","paper","scissors"])

print("--------")
print("Computer Choice:", computer_choice)

#determing the winner

#display final outputs/outcomes 


