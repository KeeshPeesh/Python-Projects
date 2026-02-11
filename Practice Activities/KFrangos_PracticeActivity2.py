# Practice Activity 1
name = input("Name: ")
age = int(input("Age: "))
print(f"Hello {name} you are {age} years old.")

# Practice Activity 2
# age = int(input("Age: "))
if age < 18:
    print("Minor")
elif age >= 18:
    print("Adult")

# Practice Activity 3
option = input("Choose an option (1, 2, or 3): ")
match option:
    case "1":
        print("You chose option 1")
    case "2":
        print("You chose option 2")
    case "3":
        print("You chose option 3")
