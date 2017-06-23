from tkinter import *
class WidgetsDemo():
    def __init__(self):
        window=Tk()
        window.title("Widgets Demo")
        frame1=Frame(window)
        frame1.pack()
        self.v1=IntVar()
        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="Red",variable=self.v2,value=1,command=self.processRadiobutton)
        rbYellow=Radiobutton(frame1,text="Yellow",variable=self.v2,value=2,command=self.processRadiobutton)
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)

        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="enter your name")
        self.name=StringVar();
        entryName=Entry(frame2,textvariable=self.name)
        btGetName=Button(frame2,text="get name",command=self.processButton)
        message=Message(frame2,text="it is a widgets demo")
        label.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=1,column=3)
        message.grid(row=1,column=4)

        text=Text(window)
        text.pack()
        text.insert(END,"Tip\nthe best way to learn thinter is ro read")
        window.mainloop()

    def processCheckbutton(self):
        print("check button is"+("checked " if self.v1.get()==1 else "unchecked"))
    def processButton(self):
        print(("red" if self.v2.get() == 1 else "Yellow")+" is selected ")
    def processRadiobutton(self):
        print("your name is "+self.name.get())
WidgetsDemo()