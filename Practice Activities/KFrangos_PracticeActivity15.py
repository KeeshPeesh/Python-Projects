class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")
class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        print(f"Students in {self.name}:")
        for student in self.students:
            student.print_info()
            
school = School("High School")
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")
student3 = Student("Charlie", "A-")
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.print_students()