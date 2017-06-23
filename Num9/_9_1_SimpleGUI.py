import tkinter
window = tkinter.Tk()
label=tkinter.Label(window,text="welcome to python")
label.pack()
button=tkinter.Button(window,text="check me")
button.pack()
# 进入消息循环
window.mainloop()