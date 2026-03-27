import random
def count_up(n, current=0):
    if current > n:
        return
    print(current)
    count_up(n, current + 1)
random_number = random.randint(0, 50)
print(f"Counting up to: {random_number}")
count_up(random_number)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
random_number = random.randint(0, 50)
print(f"Calculating factorial of: {random_number}")
print(f"Factorial of {random_number} is: {factorial_iterative(random_number)}")

# 3. The Big-O of a simple loop is O(n), where n is the number of iterations
# 4. The Big-O of a nested loop is O(n^2), where n is the number of iterations in the outer loop