# Challenge 1 Starter Code
name = "Kenshin"
age = 17
height = 1.88976

print(f"Hi {name} you are {age} years old and are {height} meters tall")

print(type(name))
print(type(age))
print(type(height))

#questions

#1. What is the difference between an int and a float?
#1 answer - int stores whole numbers, float stores decimals 

#2. Why doesn’t Python require variable type declarations?
#2 answer - python figures out the var type based on the value that its given

#3. What happens if you reassign age to a string?
#3 answer - age changes from an int to a string --> type(age) would pring str instead of int


#MODDING

nameMod = input("Name: ")
ageMod = int(input("Age: "))
heightMod = input("Height: ")

print(f"Hi {nameMod} you are {ageMod} years old and are {heightMod} meters tall")
print(f"Hi {nameMod} you are {ageMod} years old and are {heightMod} meters tall" .upper())
