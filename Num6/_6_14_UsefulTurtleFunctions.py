import turtle
turtle.speed(0)
def drawLine(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

def drawText(x,y,text):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text)

def drawPoint(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(2)

def drawCitcle(x,y,raduis):
    turtle.penup()
    turtle.goto(x,y+raduis)
    turtle.pendown()
    turtle.circle(raduis)

def drawRectangle(x,y,width,height):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)

    turtle.setheading(0)


