from tkinter import *
class MenuDemo:
    def __init__(self):
        window=Tk()
        window.title="menu demo"

        menubar=Menu(window)
        window.config(menu=menubar)



        operationMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Operation",menu=operationMenu)
        operationMenu.add_command(label="add",command=self.add)

        helperMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=helperMenu)
        helperMenu.add_command(label="about",command=self.save)


        window.mainloop()

    def add(self):
        print("menu add is check")
    def save(self):
        print("menu svae is check")
MenuDemo()