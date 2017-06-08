import turtle
import math
radius=eval(input("enter radius value:\n"))
x1,y1=eval(input("enter center point of circle:\n"))
x2,y2=eval(input("enter point:\n"))

turtle.penup()
turtle.goto(x1,y1-radius) #注意绘制箭头的方向  一旦发生改变这里要对应改变
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.circle(1)

distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
if distance<=radius:
    turtle.write("中")
else:
    turtle.write("未中");

turtle.done()