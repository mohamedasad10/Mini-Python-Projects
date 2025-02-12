class Bank():
    def __init__(self):
        self.balance = 1000000

    def show_balance(self):
        print("Balance: " + str(self.balance))
        

    def deposit(self):
        print("***********************")
        deposit_amount = input("Please enter the amount of money you would like to Deposit: ")
        self.balance = self.balance + int(deposit_amount)
        print("Your total balance is now: " + str(self.balance))

    def withdraw(self):
        print("***********************")
        withdraw_amount = input("Please enter the amount of money you would like to Withdraw: ")
        self.balance = self.balance - int(withdraw_amount)
        print("Your total balance is now: " + str(self.balance))


print("Welcome to The Bank:")
print("*****************************")
print("What would you like to do: ")
print("1. Show Balance")
print("2. Deposit")
print("3. Withdraw")
print("***************************")

num = input("Please enter a number: ")

myBank = Bank()  #Making an instance of the Bank class



if num == str(1):     
    
    myBank.show_balance()

elif num == str(2):
    myBank.deposit()

elif num == str(3):
    myBank.withdraw()

else:
    pass

    