#By Mohamed Asad Bandarkar

#Save how many times the user wins
#Save how many times the computer wins
#Using a list

import random

user_wins = 0
computer_wins = 0

options = ["rock" , "paper" , "scissors"]

while True:
    user_answer = input("Please type Rock/Paper/Scissors or q to quit: ").lower()

    if user_answer == "q":
        break

    if user_answer not in options:
        continue

    random_number = random.randint(0,2)       #rock == 0 paper == 1 scissors == 2

    computer_choice = options[random_number]

    print("The computer chose " + computer_choice )

    if user_answer == "rock" and computer_choice == "scissors":
        print("You won")
        user_wins += 1
        

    elif user_answer == "paper" and computer_choice == "rock":
        print("You won")
        user_wins += 1
        

    elif user_answer == "scissors" and computer_choice == "paper":
        print("You won")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won " + str(user_wins) + " times")     
print("The computer won " + str(computer_wins) + " times")    

        

