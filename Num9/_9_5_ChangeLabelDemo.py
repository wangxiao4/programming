from tkinter import *
class ChangeLabel():
    def __init__(self):
        window=Tk()
        window.title("Change Label Demo")
        frameTop=Frame(window)
        frameTop.pack()
        self.label=Label(frameTop,text="test text")
        self.label.grid(row=1,column=1)

        frameContent=Frame(window)
        frameContent.pack()
        labelInfo=Label(frameContent,text="enter your str")
        labelInfo.grid(row=1,column=1)
        self.stringText=StringVar()
        entryText=Entry(frameContent,text=self.stringText)
        entryText.grid(row=1,column=2)
        button=Button(frameContent,text="chang",command=self.changeText)
        button.grid(row=1,column=3)
        self.v1=IntVar()
        radioRed=Radiobutton(frameContent,variable=self.v1,value=1,text="red",command=self.changTextColor)
        radioYellow=Radiobutton(frameContent,variable=self.v1,value=2,text="yellow",command=self.changTextColor)
        radioRed.grid(row=1,column=4)
        radioYellow.grid(row=1,column=5)

        window.mainloop()
    def changeText(self):
        self.label["text"]=self.stringText.get()
    def changTextColor(self):
        if self.v1.get()==1:
            self.label["bg"]="Red"
        else:
            self.label["bg"]="Yellow"

ChangeLabel()