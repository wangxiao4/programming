from tkinter import *
class PopupMenuDemo:
    def __init__(self):
        window=Tk()
        window.title("Popup Menu Demo")

        self.menu=Menu(window,tearoff=0)
        self.menu.add_command(label="Draw a line",command=self.drawALine)
        self.menu.add_command(label="Draw a oval",command=self.drawAOval)

        self.canvas=Canvas(window,width=200,height=100,bg="#ffffff")
        self.canvas.pack()
        #这里的button-2 是指鼠标中键  1：左键   2：中键    3：右键
        self.canvas.bind("<Button-2>",self.popup)

        window.mainloop()

    def drawALine(self):
        self.canvas.create_line(0,0,200,100)
    def drawAOval(self):
        self.canvas.create_oval(0,0,200,100)
    def popup(self,event):
        self.menu.post(event.x_root,event.y_root)
PopupMenuDemo()