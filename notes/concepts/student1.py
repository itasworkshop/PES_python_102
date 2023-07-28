
class Student:

    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def myIntro(self):
        print("This is ",self.name," i scored ",self.marks)


class StudentUtility:

    def studentGradeCalculator(self,student):
        marks = student.marks

        if(marks>=90 and marks<=100):
            return {student:"A"}
        elif(marks>=80 and marks<=90):
            return {student:"B"}
        elif(marks>=70 and marks<=80):
            return {student: "C"}
        else:
            return {student:"Failed"}

st1 = Student(111,"Rajesh",75)

studentUtility = StudentUtility()
result = studentUtility.studentGradeCalculator(st1)

for i,j in result.items():
    print(i.name," my grade is ",j)