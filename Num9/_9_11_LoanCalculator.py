from tkinter import *
class LoanCalculator:
    def __init__(self):
        window=Tk()
        window.title("loam calculator")

        Label(window,text="annual interest rate").grid(row=1,column=1)
        self.str1=StringVar()
        Entry(window,textvariable=self.str1).grid(row=1,column=2)
        Label(window,text="number of year").grid(row=2,column=1)
        self.str2=StringVar()
        Entry(window,textvariable=self.str2).grid(row=2,column=2)
        Label(window,text="loan amount").grid(row=3,column=1)
        self.num1=StringVar()
        Entry(window,textvariable=self.num1).grid(row=3,column=2)
        Label(window,text="monthly payment").grid(row=4,column=1)
        self.num2=StringVar()
        Label(window,textvariable=self.num2).grid(row=4,column=2)
        Label(window,text="total payment").grid(row=5,column=1)
        self.num3=StringVar()
        Label(window,textvariable=self.num3).grid(row=5,column=2)

        Button(window,text="compute payment",command=self.computePayment).grid(row=6,column=2)

        window.mainloop()
    def computePayment(self):
        monthlyPayment=self.getMonthlyPayment(float(self.num1.get()),float(self.str1.get())/1200,int(self.str2.get()))
        self.num2.set(format(monthlyPayment,"10.2f"))
        totalPayment=float(self.num2.get())*12*float(self.num1.get())
        self.num3.set(format(totalPayment,"10.2f"))

    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberOfYears):

        monthlyPayment=loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))
        print(monthlyPayment)
        return monthlyPayment


LoanCalculator()