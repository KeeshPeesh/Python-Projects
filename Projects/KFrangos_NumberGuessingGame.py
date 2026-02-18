import random

number = random.randint(1, 100)
attempts = 10
used_attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while attempts > 0:
    # error handling
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    used_attempts += 1

    # guessing logic
    if guess < number:
        print("Too low! Attempts left:", attempts - 1)
    elif guess > number:
        print("Too high! Attempts left:", attempts - 1)
    else:
        print("Congratulations! You've guessed the number in", used_attempts, "attempts!")
        break

    attempts -= 1

if attempts == 0:
    print("You've run out of attempts. The number was", number)
