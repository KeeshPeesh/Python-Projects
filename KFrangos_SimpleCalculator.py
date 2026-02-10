import math

while True:
    #first number
    num1 = input("Enter first number or type 'stop' to stop: ")
    if num1 == "stop":
        break

    #error handling
    try:
        num1 = int(num1)
    except:
        print("Invalid input. Please enter an number.")
        continue

    #operator
    operator = input("Enter operator (+, -, *, /, ^, sqrt): ")

    #square root
    if operator == "sqrt":
        print(math.sqrt(num1))
        continue
    
    #second number
    num2 = input("Enter second number: ")

    #error handling
    try:
        num2 = int(num2)
    except:
        print("Invalid input. Please enter an number.")
        continue
    
    #operations
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)

    if operator == "/" and num2 == 0:
        print("Cannot divide by zero")
    elif operator == "/":
        print(num1 / num2)
    
    elif operator == "^":
        print(num1 ** num2)
        
        #invalid operator
    else:
        if operator not in ["+", "-", "*", "/", "^", "sqrt"]:
            print("Invalid operator")