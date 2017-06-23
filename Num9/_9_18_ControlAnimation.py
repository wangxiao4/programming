from tkinter import *
class AnimationDemo:
    def __init__(self):

        self.isMove=False
        self.x_Speed=1
        self.y_Speed=1

        window=Tk()
        window.title("Animation demo")


        width=250
        height=150

        canvas=Canvas(window,width=width,height=height)

        self.testText_x=10
        self.testText_y=10
        testText=canvas.create_text(self.testText_x,self.testText_y,text="天上飘着五个字",tags="text")
        canvas.pack()

        startButton=Button(window,text="开始",command=self.StartMove)
        startButton.pack(side=LEFT)
        startButton=Button(window,text="加速",command=self.MoveSpeedAdd)
        startButton.pack(side=LEFT)
        startButton=Button(window,text="减速",command=self.MoveSpeedSub)
        startButton.pack(side=LEFT)
        startButton=Button(window,text="停止",command=self.StopMove)
        startButton.pack(side=LEFT)

        x_f=1
        y_f=1

        while True:
            if self.isMove:
                if self.testText_x>=width or self.testText_x<=0:
                    x_f=x_f*-1
                if self.testText_y>=height or self.testText_y<=0:
                    y_f=y_f*-1
                self.testText_y=self.testText_y+self.y_Speed*y_f
                self.testText_x=self.testText_x+self.x_Speed*x_f
                canvas.move("text",self.x_Speed*x_f,self.y_Speed*y_f)
                print(self.testText_x,self.testText_y)

            canvas.after(100)
            canvas.update()


        window.mainloop()

    def StartMove(self):
        self.isMove=True
    def MoveSpeedAdd(self):
        self.x_Speed=self.x_Speed+1
        self.y_Speed=self.y_Speed+1
    def MoveSpeedSub(self):
        self.x_Speed=self.x_Speed-1
        self.y_Speed=self.y_Speed-1
    def StopMove(self):
        self.isMove=False


AnimationDemo()