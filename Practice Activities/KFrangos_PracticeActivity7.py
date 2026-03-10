scores = [90, 81, 77, 65, 55, 94, 33, 78, 78, 84]

total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Average: {average:.2f}")

doubled = [score * 2 for score in scores]
print(f"Doubled: {doubled}")

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"1: {values[0]}")
print(f"2: {values[1]}")
print(f"3: {values[2]}")