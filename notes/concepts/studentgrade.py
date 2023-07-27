
students = {"raj":75,"suraj":68,"Tom":87}
students_with_grade = {}

for i,j in students.items():
    marks = j
    if (marks >= 90 and marks <= 100):
        students_with_grade[i] = "A"
    elif (marks >= 80 and marks <= 90):
        students_with_grade[i] = "B"
    elif (marks >= 70 and marks <= 80):
        students_with_grade[i] = "C"
    else:
        students_with_grade[i] = "Failed"

print(students_with_grade)