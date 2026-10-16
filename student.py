import sys
def calculate_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=55:
         return "C"
    elif marks>=35:
        return "D"
    else:
        return "F"
def display_grade(name,marks):
    grade=calculate_grade(marks)
    print("student name:",name)
    print("marks:",marks)
    print("Grade:",grade)

name=float(input(sys.argv[1]))
marks=float(input(sys.argv[2]))
if name=="":
    name=="student"
    if marks=="":
        marks=""
  
display_grade(name,marks)