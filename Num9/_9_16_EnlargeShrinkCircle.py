from tkinter import *
class EnlargeShrinkCircle:
    def __init__(self):
        window=Tk()
        window.title("Enlarge Shrink Circle")

        self.canvas=Canvas(window)
        self.canvas.bind("<Button-1>",self.LeftButtonDown)
        self.canvas.bind("<Button-3>",self.RightButtonDown)
        self.radius=50
        self.DisplayCircle()
        self.canvas.pack()

        window.mainloop()

    def LeftButtonDown(self,enevt):
        self.radius = self.radius+1
        self.DisplayCircle()
    def RightButtonDown(self,enevt):
        self.radius = self.radius-1
        self.DisplayCircle()
    def DisplayCircle(self):
        self.canvas.delete("oval")
        self.canvas.create_oval(10,10,self.radius,self.radius,fill="red",tags="oval")

EnlargeShrinkCircle()