import turtle
x1,y1=eval(input("enter x1 & y1 for point1:"))
x2,y2=eval(input("enter x2 & y2 for point2:"))
distance=((x2-x1)**2+(y2-y1)**2)**(1/2)

turtle.penup();
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("point1")
turtle.goto(x2,y2)
turtle.write("point2");
turtle.done()