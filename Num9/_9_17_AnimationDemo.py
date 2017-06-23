from tkinter import *
class AnimationDemo:
    def __init__(self):
        window=Tk()
        window.title("Animation demo")


        width=250
        height=150

        canvas=Canvas(window,width=width,height=height)

        self.testText_x=10
        self.testText_y=10
        testText=canvas.create_text(self.testText_x,self.testText_y,text="天上飘着五个字",tags="text")
        canvas.pack()

        x_f=1
        y_f=1
        while True:
            x_temp=1
            y_temp=1
            if self.testText_x>=width or self.testText_x<=0:
                x_f=x_f*-1
            if self.testText_y>=height or self.testText_y<=0:
                y_f=y_f*-1
            self.testText_y=self.testText_y+y_temp*y_f
            self.testText_x=self.testText_x+x_temp*x_f
            canvas.move("text",x_temp*x_f,y_temp*y_f)
            canvas.after(10)
            canvas.update()
            print(self.testText_x,self.testText_y)


        window.mainloop()

AnimationDemo()