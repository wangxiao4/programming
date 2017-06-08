def printGrade(score):
    grade="F"
    if score<60:
        grade = ("F")
    elif score<70:
        grade = ("D")
    elif score<80:
        grade = ("C")
    elif score<90:
        grade =("B")
    else:
        grade =("A")
    return grade

score=eval(input("enter score\n"))
print(printGrade(score))