class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def show_info(self):
        print(self.name, self.student_id, self.major)


student1 = Student("Setareh", 101, "AI")
student2 = Student("Sepideh", 102, "Computer")

student1.show_info()
student2.show_info()