import random
import turtle
import math

#绘制格子
rowCount=15
rowStep=20
temp_MaxValue=rowCount*rowStep

temp_value=-1*(rowCount*rowStep)
turtle.speed(0)
turtle.color("green")
while temp_value<=temp_MaxValue:
    turtle.penup()
    turtle.goto(temp_value,-1*temp_MaxValue)
    turtle.pendown()

    turtle.goto(temp_value,temp_MaxValue)

    turtle.penup()
    turtle.goto(-1*temp_MaxValue,temp_value)
    turtle.pendown()

    turtle.goto(temp_MaxValue,temp_value)

    temp_value+=rowStep

#回原点
x=0
y=0
turtle.penup()
turtle.goto(x,y)
turtle.pendown()

turtle.speed(1)
turtle.color("red")
turtle.pensize(3)

while 1==1:
    rand_forword=random.randint(0,4)
    if rand_forword==0:
        x+=random.randint(1,5)*(rowStep/2)
    elif rand_forword==1:
        x-=random.randint(1,5)*(rowStep/2)
    elif rand_forword==2:
        y+=random.randint(1,5)*(rowStep/2)
    elif rand_forword==3:
        y-=random.randint(1,5)*(rowStep/2)
    turtle.goto(x,y)
    if(math.fabs(x)>temp_MaxValue or math.fabs(y)>temp_MaxValue):
        break



turtle.done()