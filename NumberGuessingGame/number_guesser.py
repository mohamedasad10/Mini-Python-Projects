#22/05/2024
#Generate a random number
#Track how many times it takes the user to guess this number

import random

random_number = random.randint(0,10)

#guessed_number = input("Please enter your number from 1 - 10: ")

counter = 0    #Tracks how many times it took the user to guess the correct answer

while True:
    guessed_number = input("Please enter your number from 1 - 10: ")
    if random_number == int(guessed_number):
        counter =+ 1
        print("You are correct!")
        print("You took " + str(counter) + " tries to get to the correct random number.")
        

    elif int(guessed_number) < random_number:
        print("The guessed number is LOWER than the random number")
        counter =+ 1

    elif int(guessed_number) > random_number:
        print("The guessed number is HIGHER than the random number")
        counter =+ 1
        
    else:
        print("Try again...")
        counter =+ 1
          
        