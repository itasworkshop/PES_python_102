
class Student:

    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def myIntro(self):
        print("This is ",self.name," i scored ",self.marks)

st1 = Student(111,"Rajesh",75)

def studentGradeCalculator(student):
    marks = student.marks

    if(marks>=90 and marks<=100):
        print("A grade")
    elif(marks>=80 and marks<=90):
        print("B grade")
    elif(marks>=70 and marks<=80):
        print("C grade")
    else:
        print("Failed")


studentGradeCalculator(st1)