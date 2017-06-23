from tkinter import *

class MouseKey:
    def __init__(self):
        window=Tk()
        window.title("Mouse key event demo")

        canvas=Canvas(window)
        canvas.bind("<Button-1>",self.mouseDown)
        canvas.bind("<Key>",self.keyDown)
        canvas.focus_set()
        canvas.pack()

        window.mainloop()

    def mouseDown(self,enevt):
        print("mouse position in canvas:",enevt.x,enevt.y)
        print("mouse position in screen:",enevt.x_root,enevt.y_root)
        print("mouse number is:",enevt.num)

    def keyDown(self,enevt):
        print("key char is:",enevt.char)
        print("key keycode is:",enevt.keycode)
        print("key keysym is:",enevt.keysym)

MouseKey()