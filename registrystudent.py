class Student:
    def __init__(self, name, gpa, gradeyear):
        self.name = name
        self.gpa = gpa
        self.gradeyear = gradeyear

    def myfunc(self):
        print("Student Info: " + self.name + str(self.gpa) + str(self.gradeyear))

student1 = Student("Emma", 3.95, 4)

student1.myfunc()