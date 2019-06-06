##game.py
#
#import random
#
#print("Rock, Paper, Scissors, Shoot!")  
#
##capture input
#
#user_choice = input("Please chose one of the following options: 'rock', 'paper' or 'scissors' (without the quotes):")
#
#print("----------")
#print("User chose:",user_choice)
#
#
##validate input
#
#options = ["rock","paper","scissors"]
#
#if user_choice not in options:     
#    print("Invalid Selection Please Try Again")
#    exit()
#
##generate computer selection
#print("Generating...") 
#
#computer_choice = random.choice(["rock","paper","scissors"])
#
#print("--------")
#print("Computer Choice:", computer_choice)
#
##determing the winner
#
##rocks beats scissors
##paper beats rock
##scissors beats paper
##same selection is a tie
#
#if user_choice == computer_choice:
#    print("Its a tie!")
#elif user_choice == "rock" and computer_choice == "paper":
#    print("Paper")
#elif user_choice == "rock" and computer_choice == "scissors":
#    print("Rock")
#
#elif user_choice == "paper" and computer_choice == "rock":
#    print("paper")
#elif user_choice == "paper" and computer_choice == "scissors":
#    print("scissors")
#
#elif user_choice == "scissors" and computer_choice == "paper":
#    print("scissors")
#elif user_choice == "scissors" and computer_choice == "rock":
#    print("rock")
#
##display final outputs/outcomes 

# game.py

import random

def my_message():
    return "Hello"

x = my_message

if __name__ == "__main__":

    print("Rock, Paper, Scissors, Shoot!") # this is also a comment

    # CAPTURE INPUTS

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("--------------")
    print("USER CHOICE:", user_choice)

    # VALIDATE INPUTS

    options = ["rock", "paper", "scissors"]

    if user_choice not in options:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
        exit()

    # GENERATE COMPUTER SELECTION

    computer_choice = random.choice(options)

    print("--------------")
    print("GENERATING...")
    print("COMPUTER CHOICE:", computer_choice)

    # DETERMINE THE WINNER
    #
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    # same selections is a tie
    #
    # first attribute represents the user, second represents the computer
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winning_choice = winners[user_choice][computer_choice]

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")

    print("Thanks for playing. Please play again!")
