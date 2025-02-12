
def Expense():
    global budget
    expense_description = input("Enter expense description: ")
    expense = int(input("Enter expense amount: "))
    budget = budget - expense
    

def Budget_details():
    print(budget)

budget = int(input("Please enter your budget"))


while True:
    print("What would you like to do: ")
    print("1. Add an Expense")
    print("2. Show budget details")
    print("3. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        Expense()

    elif choice == "2":
        Budget_details()

    elif choice == "3":
        break 

    else:
        print("Please enter a valid choice!")
        
