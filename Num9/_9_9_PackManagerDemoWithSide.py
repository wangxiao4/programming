from tkinter import *
class PackManagerDemoWithSide:
    window=Tk()
    window.title="pack manager demo with side"

    Label(window,text="blue",bg="blue").pack(side=RIGHT)
    Label(window,text="red",bg="red").pack(fill=BOTH,expand=2,side=RIGHT)
    Label(window,text="Blue",bg="blue").pack(side=RIGHT,fill=BOTH)

    window.mainloop()

PackManagerDemoWithSide()