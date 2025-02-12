import random

COLORS = ["R" , "G" , "B" , "Y" , "O" , "W"]
TRIES = 10
CODE_LENGTH = 4 #This is the number of colors the user must guess(eg. R O W G)

#Generate Colors
def generate_code():
    code = []                #List

    #this for loop runs for CODE_LENGTH times and appends the color into the code list
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)     #selects random colors
        code.append(color)

    return code    

#User Guess
def guess_code():
    guess = input("Guess: ").upper().split(" ")  #split takes user input: R G Y B --> ["R","G","Y","B"]

    while True:
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break 

    return guess    

#Check how many are correct
def check_code(guess,real_code):
    color_counts = {}   #dictionary
    correct_position = 0
    incorrect_position = 0

    for color in real_code:
        if color not in color_counts:   #if that color is not a key in the dictionary
            color_counts[color] = 0     #then add it and set that particular key to 0
        color_counts[color] += 1       #increment the count for that particular color in the dictionary   

    #Zip function: guess = ["G","R"] |||real  = ["W","Y"]||| [("G","W") , ("R","Y")]
    for guess_color ,real_color in zip(guess,real_code): 
        if guess_color == real_color:
            correct_position += 1
            color_counts[guess_color] -= 1            #remove the color from the dictionary


    for guess_color ,real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position += 1
            color_counts[guess_color] -= 1

    return correct_position, incorrect_position

def game():
    print(f"Welcome to Mastermind. You have {TRIES} to guess the colors.")
    print("The valid colors are ", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess,code)

        if correct_position == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct positions: {correct_position} | Incorrect positions: {incorrect_position}")

    else:
        print("You ran out of tries, the code was: ", *code)



if __name__ == "__main__":
    game()