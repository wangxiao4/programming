class Loan:
    def __init__(self,annualIntersestRate,numberOfYear = 1,locnAmount=1000,borrower=" "):
        self.__annualIntersestRate=annualIntersestRate
        self.__numberOfYear=numberOfYear
        self.__locnAmount=locnAmount
        self.__borrower=borrower

    def getAnnualInterestRate(self):
        return self.__annualIntersestRate
    def getNumberOfYears(self):
        return self.__numberOfYear
    def getLoanAmount(self):
        return self.__locnAmount
    def getBorrwer(self):
        return self.__borrower
    def setAnnualInterestRate(self,annualIntersestRate):
        self.__annualIntersestRate=annualIntersestRate
    def setNumberOfYears(self,numberOfYear):
        self.__annualNumberOfYears=numberOfYear
    def setLocnAmount(self,locnAmount):
        self.__locnAmount=locnAmount
    def setBorrower(self,borrower):
        self.__borrower=borrower
    def getMonthlyPayment(self):
        monthlyInerestRate=self.__annualIntersestRate/1200
        monthlyPayment=self.__locnAmount*monthlyInerestRate/(1-(1/(1+monthlyInerestRate)**(self.__numberOfYear*12)))
        return monthlyPayment
    def getTotalPayment(self):
        totalPayment=self.getMonthlyPayment()*self.__numberOfYear*12
        return totalPayment

