class Student:
    def __init__(selef,name,student_id):
        selef.name = name
        selef.student_id = student_id
        selef.grades = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 20:
            print("Invallid grade")
        else:
            self.grades[course] = grade

    def average(self):
        if len(self.add_grades) == 0:
            return 0
        
        total = sum(self.grades.values())
        return total / len(self.grades)
    
    def best_course(self):
        if len(self.grades) == 0:
            return None
        
        return max(self.grades, key=self.grades.get)
    
    def failed_courses(self):
        failed = []

        for course , grade in self.grades.items():
            if grade < 10:
                failed.append(course)

        return failed
    
    def status(self):
        avg = self.average()

        if avg > 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"
        
    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")

        for course, grade in self.grades.items():
            print(f"{course}: {grade}")


            print(f"Average: {self.average()}")
            print(f"Best course: {self.best_course()}")
            print(f"Failed courses: {self.failed_courses()}")
            print(f"Status: {self.status()}")

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if len(self.students) ==0:
            return None
        
        return max(self.students, key=lambda student: student.average())
    
    def class_average(self):
        if len(self.students) == 0:
            return 0
        
        total = 0

        for student in self.students:
            total += student.average()

        return total / len(self.students)
    
sara = Student("Sara Ahmadi", "40312345")
ali = Student("Ali Rezaei", "40312346")

sara.add_grade("Math", 18)
sara.add_grade("Physics", 9)
sara.add_grade("Programming", 20)
sara.add_grade("English", 15)

ali.add_grade("Math", 16)
ali.add_grade("Physics", 14)
ali.add_grade("Programming", 17)
ali.add_grade("English", 13)

sara.report()

print()

classroom = Classroom()

classroom.add_student(sara)
classroom.add_student(ali)

top = classroom.top_student()

print("Top student:", top.name)
print("Class average:", classroom.class_average())