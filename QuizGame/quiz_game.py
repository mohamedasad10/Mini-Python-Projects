#Ask 10 questions
#If user gets question correctly, then add 1 to the score
#Printout final score at the End

print("Welcome to the Quiz Game.")
score = 0
print("Question 1: Who does CR7 play for?")
answer_Q1 = input("Answer: ")

if answer_Q1 == "Al-Nassr":
    print("Correct!")
    score += 1 

else:
    print("Incorrect")


####################QUESTION 2########################################
print("Question 2: In which team did CR7 score the most goals?")
answer_Q2 = input("Answer: ")

if answer_Q2 == "Real Madrid":
    print("Correct!")
    score += 1 

else:
    print("Incorrect")


print("Your final score is " + str(score))