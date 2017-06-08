annualInterestRate=eval(input("Enter annual interest rate,e.g.,7.25:"))
monthlyInterestRate=annualInterestRate/1200
numberOgYears=eval(input("Enter number of years as an integer:"))
loanAmount=eval(input("Enter loan amount:"))
monthlyPayment=loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOgYears*12))
totalPayment=monthlyPayment*numberOgYears*12
print("the monthly payment is",int(monthlyPayment*100)/100)
print("the total payment is",int(totalPayment*100)/100)
