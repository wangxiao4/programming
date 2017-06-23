import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

tkinter.messagebox.showinfo("showinfo","message")
tkinter.messagebox.showwarning("showwarning","warning")
tkinter.messagebox.showerror("showerror","error")
isYes=tkinter.messagebox.askyesno("askyesno","message")
print(isYes)

isOK=tkinter.messagebox.askokcancel("askokcancel","ok?")
print(isOK)

isYesNoCancel=tkinter.messagebox.askyesnocancel("askyesnocancel","yes,no,cancel?")
print(isYesNoCancel)

name=tkinter.simpledialog.askstring("askstring","enter your name")
print(name)

age=tkinter.simpledialog.askinteger("askinteger","enter your age")
print(age)

weight=tkinter.simpledialog.askfloat("askfloat","enter your weight")
print(weight)