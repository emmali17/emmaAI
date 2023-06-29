class Course:
    def course(self, teachername, coursename):
        self.teachername = teachername
        self.coursename = coursename

    def myfunc(self):
        print("Course information: " + self.teachername + self.coursename)
    
    if __name__ == "__main__":
        print("yeah")