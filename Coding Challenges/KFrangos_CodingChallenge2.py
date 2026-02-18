# Challenge 2 Starter Code
user_input = input("Enter a word: ")

print("Word (Lowercase):", user_input.lower())
print("Word (Length)", len(user_input))

if len(user_input) > 5:
    print("Long word")
else:
    print("short word")
    
    
print("Word (Uppercase):", user_input.upper())

#questions
#1. What does len() return?
#1 answer - it returns the number of characters of a string

#2. Why must input be cast before math operations?
#2 answer - input is a string, it has to be cast to a int or float before you can use it for math operations

#3. What operator checks equality?
#3 answer - == checks for equality

#MODDING
#● Check if the word is a palindrome
#● Count vowels in the word

#palindrome check
if user_input == user_input[::-1]:
    print("The word is a palindrome")
    
#vowel count
vowels = "aeiouAEIOU"
vowelCount = 0

for char in user_input:
    if char in vowels:
        vowelCount += 1
        
print("Vowels:", vowelCount)