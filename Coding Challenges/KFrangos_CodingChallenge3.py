# Challenge 3 Starter Code
numbers = []

for i in range(5):
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

for num in numbers:
    print(num)

total = sum(numbers)
average = total / len(numbers)

print(f"The sum of the numbers is: {total}")
print(f"The average of the numbers is: {average}")

#questions

#1. What causes a ValueError?
#1 answer - a function gets a argument of the right type but a wrong value

#2. Difference between while and for loops?
#2 answer - for loop = iterate a sequence of items. while loop = repeat a block of code as long as a condiition is true

#3. Why is error handling important?
#3 answer - error handling is important because it lets a program continue to run when it has an error instead of crashing


#MODDING

numbers = []
while True:
    user_input = input("Enter a number ('q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        num = int(user_input)
        if num < 0:
            print("Negative numbers are not allowed. Please enter a positive integer.")
            continue
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")