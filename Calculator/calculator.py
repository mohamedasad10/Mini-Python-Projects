#Calculator using Python

def add(x,y):
    z = int(x) + int(y)
    return z 

def subtract(x,y):
    z = int(x) - int(y)
    return z

def multiply(x,y):
    z = int(x) * int(y) 
    return z

def divide(x,y):
    z = int(x) / int(y)
    return z

x = input("Number 1: ")
y = input("Number 2: ")

print("Would you like to +, - , *, / ?")
operation = input("Operation: ")

if operation == "+":
    z = add(x,y)
    print(z)

elif operation == "-":
    z = subtract(x,y)
    print(z)

elif operation == "*":
    z = multiply(x,y)
    print(z)

elif operation == "/":
    z = divide(x,y)
    print(z)

