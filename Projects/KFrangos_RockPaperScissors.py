import random

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Select your move (1, 2, or 3):")
    try:
        user = int(input())
        if user in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3")
    except ValueError:
        print("Invalid input. Please enter a number")

if user == 1:
    user_move = "Rock"
elif user == 2:
    user_move = "Paper"
else:
    user_move = "Scissors"

print("You selected:", user_move)

cpu = random.randint(1, 3)
if cpu == 1:
    cpu_move = "Rock"
elif cpu == 2:
    cpu_move = "Paper"
else:    cpu_move = "Scissors"

print("Computer selected:", cpu_move)
if user == 1:
    if cpu == 2:
        print("You lose! Paper beats rock.")
    elif cpu == 3:
        print("You win! Rock beats scissors.")

elif user == 2:
    if cpu == 1:
        print("You win! Paper beats rock.")
    elif cpu == 3:
        print("You lose! Scissors beats paper.")

elif user == 3:
    if cpu == 1:
        print("You lose! Rock beats scissors.")
    elif cpu == 2:
        print("You win! Scissors beats paper.")

if user == cpu:
    print("It's a tie.")
    