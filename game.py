

import random

user_action = input("Choose (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]



if user_action not in possible_actions:
    print("Oops. Invalid Entry.")
    quit()
    
computer_action = random.choice(possible_actions)
print("You chose", user_action)
print("Computer chose", computer_action)

# I got some help from out notes from class and also from real python.com
if user_action == computer_action:
    print("Both players selected", user_action, "You tied.")
#need to input some validity function


elif user_action == "scissors":
    if computer_action == "paper":
        print("You win!")
    else:
        print("You lose!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_action == "paper":
    if computer_action == "scissors":
       print("You lose!")
    else:
        print("You win!")
