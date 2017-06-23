#9.1    turtle适合绘制  tkinter适合交互
#9.2    引入tkinter Tk() mainloop()
#9.3    循环监听
#9.4    父容器
#9.5    绑定事件
#9.6    Label(window,text="welcome",fg="#ffffff",bg="#000000")
#9.7    Button(window,text="OK",fg="#ffffff",bg,="red",command=processOK)
#9.8    Radiobutton(window,text="apple",fg="ffffff",bg="red",variable=v1,command=processApple)
#9.9    Checkbutton(window,text="senior",fg="ffffff",bg="red",variable=v1,command=processSenior)
#9.10   Entry(window,variable=v1,fg="ffffff",bg="red")
#9.11   Message(window,fg="ffffff",bg="red",text="programming is fun")
#9.12   left center right
'''
from tkinter import *
print(LEFT,CENTER,RIGHT)
'''
#9.13   create_line(34,50,50,90)
#9.14   create_ranganle(20,20,10,10,fill="red")
#9.15   create_arc(-30,20,fill="red")
#9.16   create_arc(-30,-30,80,80,start=30,extent=45)
#9.17   create_polygo(10,10,15,30,140,10,10,100,fill="red")
#9.18   width=size
#9.19   arrow="last",activefill="blue"
#9.20   activefill=color

#9.21   缺少 side （side=LEFT）
#9.22   包管理器
#9.23   因为各种平台环境不一致可能导致效果不一致
#9.24   x y both s n e w nw ne sw se
from tkinter import *
print(X,Y,BOTH,S,N,E,W,NW,NE,SW,SE)

#9.25   PhotoImage只能处理gif图片
#9.26   缺少file关键字
#9.27   image=PhotoImage(file="路径") button=Button(window,image=image)

#9.28   Menu
#9.29   menu.post(event.x_root,event.y_root)

#9.30   bind("<Button-i>",p)
#9.31   <B3-Motion>
#9.32   <Double-Button-i>
#9.33   <Triple-Button-2>
#9.34   enevt(事件)
#9.35   enevt.x enevt.y
#9.36   enevt.char

#9.37   canvase.after(毫秒)
#9.38   canvas.update()

#9.39   Text/Canvas/Listbox
#9.40   yscrollcommand设置关联的scroll.set  scroll.config()设置滚动条关联的轴向
#9.41   tkinter.messagebox.showinfo("info","Welcome to Python")
#9.42   ……

