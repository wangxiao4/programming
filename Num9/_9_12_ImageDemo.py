from tkinter import *
class ImageDemo:
    def __init__(self):
        window=Tk()
        window.title("Image demo")

        opcImage=PhotoImage(file="Imgs/dog.gif")
        xwzImage=PhotoImage(file="Imgs/dog1.gif")

        #PhotoImage 只能处理gif 图片 且无法显示动态

        freeForJobImage=PhotoImage(file="Imgs/free_for_job.png")
        databaseImage=PhotoImage(file="Imgs/database.png")
        freelanceImage=PhotoImage(file="Imgs/freelance.png")
        sign_inImage=PhotoImage(file="Imgs/sign_in.png")
        sign_outImage=PhotoImage(file="Imgs/sign_out.png")
        worldImage=PhotoImage(file="Imgs/world.png")

        frame1=Frame(window)
        frame1.pack()
        Label(frame1,image=opcImage).pack(side=LEFT)
        canvas=Canvas(frame1)
        canvas.create_image(90,50,image=xwzImage)
        canvas["width"]=200
        canvas["height"]=100
        canvas.pack(side=LEFT)

        window.mainloop()
ImageDemo()

