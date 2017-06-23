from tkinter import *
class PlaceManagerDemo:
    def __init__(self):
        window=Tk()
        window.title("plcae manager demo")

        Label(window,text="blue",bg="blue").place(x=20,y=20)
        Label(window,text="red",bg="red").place(x=40,y=40)
        Label(window,text="green",bg="green").place(x=60,y=60)

        window.mainloop()

PlaceManagerDemo()
