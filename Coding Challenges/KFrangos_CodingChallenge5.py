# Challenge 5 Starter Code
students = ["Jay", "Nick", "Alex", "Diego", "Noah", "Logan"]

removed_students = set(students)

student_grades = {
    "Jay": 85,
    "Nick": 78,
    "Alex": 92,
    "Diego": 65,
    "Noah": 88,
    "Logan": 73
}

print("Students with grades above 70:")
for student, grade in student_grades.items():
    if grade > 70:
        print(student)

#questions

#1. Difference between list and tuple?
#1 answer - a list can be changed after its made, a tuple cannot be changed

#2. Why are sets unordered?
#2 answer - they are implemented as hash tables

#3. When should dictionaries be used?
#3 answer - to store data in pairs of keys and values


#MODDING
total_grade = sum(student_grades.values())
class_average = total_grade / len(student_grades)
print(f"Class average: {class_average:.2f}")

sorted_students = sorted(student_grades.items(), key=lambda x: x[1], reverse=True)
print("Students sorted by grade:")
for student, grade in sorted_students:
    print(f"{student}: {grade}")