import _7_1_Circle

def main():
    circle = _7_1_Circle.Circle(5)
    printCircle(circle,5)

def printCircle(c,count):

    while count>0:
        print(count,"\t\t",c.getArea())
        c.radius-=1
        count-=1
main()