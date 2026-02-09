import math

while True:
    num1 = input("Enter first number or type stop to stop: ")
    if num1 == "stop":
        break
    num1 = int(num1)
    
    operator = input("Enter operator (+, -, *, /, ^, √): ")
    
    if operator == "√":
        print(math.sqrt(num1))
        continue
    
    num2 = int(input("Enter second number: "))
    
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
    else:
        print("Invalid operator")
        