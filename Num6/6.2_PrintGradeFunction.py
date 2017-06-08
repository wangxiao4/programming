def printGrade(score):
    if score<60:
        print("F")
    elif score<70:
        print("D")
    elif score<80:
        print("C")
    elif score<90:
        print("B")
    else:
        print("A")

score=eval(input("enter score\n"))
printGrade(score)