from tkinter import *
from random import randint

def GetRandomPosition(minX=0,minY=0,maxX=1,maxY=1):
    return randint(minX,maxX),randint(minY,maxY)
def GetRandomColor():
    hexColor=""
    for i in range(0,6):
        temp=randint(0,15)
        if(temp>9):
            temp=ord('A')+(temp-10)
        else:
            temp=ord('0')+temp
        hexColor+=chr(temp)
    return hexColor

#print (GetRandomColor())
#print (GetRandomPosition(maxX=350,maxY=150))

class Ball:
    def __init__(self,width,height):
        self.x,self.y=GetRandomPosition(maxX=width,maxY=height)
        self.dx,self.dy=GetRandomPosition(minX=-5,minY=-5,maxX=5,maxY=5)
        self.color="#"+GetRandomColor()
        self.radius=randint(3,7)

#print(Ball(350,150))

class BounceBalls:
    def __init__(self):
        self.ballList=[]
        self.state=False
        self.sleepTime=1000//60

        window=Tk()
        window.title="Bounce in balls"

        self.width=350
        self.height=150
        self.canvas=Canvas(window,bg="#ffffff",width=self.width,height=self.height)
        self.canvas.pack()

        frame=Frame(window)
        frame.pack()
        btStart=Button(frame,text="Start",command=self.start).pack(side=LEFT)
        btStop=Button(frame,text="Stop",command=self.stop).pack(side=LEFT)
        btAdd=Button(frame,text="+",command=self.add).pack(side=LEFT)
        btSub=Button(frame,text="-",command=self.sub).pack(side=LEFT)

        self.animate()

        window.mainloop()

    def start(self):
        self.state=True
        self.animate()

    def stop(self):
        self.state=False

    def add(self):
        self.ballList.append(Ball(self.width,self.height))

    def sub(self):
        self.ballList.pop()

    def animate(self):
        while self.state:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("ball")

            self.updateBall()

    def updateBall(self):
        for i in range(len(self.ballList)):
            if(self.ballList[i].x>self.width or self.ballList[i].x<0):
                self.ballList[i].dx*=-1
            if(self.ballList[i].y>self.height or self.ballList[i].y<0):
                self.ballList[i].dy*=-1
            self.ballList[i].x+=self.ballList[i].dx
            self.ballList[i].y+=self.ballList[i].dy
            self.canvas.create_oval(self.ballList[i].x-self.ballList[i].radius,self.ballList[i].y-self.ballList[i].radius,self.ballList[i].x+self.ballList[i].radius,self.ballList[i].y+self.ballList[i].radius,fill=self.ballList[i].color,tag="ball")
        return

BounceBalls()