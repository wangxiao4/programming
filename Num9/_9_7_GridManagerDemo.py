from tkinter import *
class GridManagerDemo:
    window=Tk()
    window.title("grid manager demo")

    message=Message(window,text="this message widget occupoes three rows and tow columns")
    message.grid(row=1,column=1,rowspan=3,columnspan=2)
    Label(window,text="first name:").grid(row=1,column=3)
    Entry(window).grid(row=1,column=4,padx=5,pady=5)
    Label(window,text="last name:").grid(row=2,column=3)
    Entry(window).grid(row=2,column=4)
    Button(window,text="Get Name").grid(row=3,padx=5,pady=5,column=4,sticky=E)

    window.mainloop()

GridManagerDemo()
