from tkinter import *

def processOK():
    print("ok button is checked")
def processCancel():
    print("Cancel button is checked")

window=Tk()
btok=Button(window,text="ok",fg="red",command=processOK)
btCancel=Button(window,text="Cancel",bg="yellow",command=processCancel)
btok.pack()
btCancel.pack()

window.mainloop()