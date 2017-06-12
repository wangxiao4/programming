from _7_8_Loan import Loan

def main():
    annualInterestRate=eval(input("enter yearly interset rate , for example,7.25:"))
    numberOfyears=eval(input("enter number of years as integer:"))
    locnAmount=eval(input("enter loan amount,for example,120000.95"))
    borrower = input("enter a borrwer's name:")
    loan=Loan(annualInterestRate,numberOfyears,locnAmount,borrower)
    print("the loan is for",loan.getBorrwer())
    print("the monthly payment is ",loan.getMonthlyPayment())
    print("the toeal payment is",loan.getTotalPayment())

main()