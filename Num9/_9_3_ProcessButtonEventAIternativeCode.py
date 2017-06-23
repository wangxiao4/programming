from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        window=Tk()
        btOk=Button(window,text="ok",fg="red",command=self.processOK)
        btOk.pack()
        btCancel=Button(window,text="Cancel",bg="yellow",command=self.processCancel)
        btCancel.pack()
        window.mainloop();
    def processOK(self):
        print("Ok button is check")
    def processCancel(self):
        print("Cancel button is check")

ProcessButtonEvent()