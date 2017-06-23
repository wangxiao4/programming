class Rational:
    def __init__(self,numerator=1,denominator=0):
        divisor=gcd(numerator,denominator)
        self.__numerator=(1 if denominator>0 else -1)*int(numerator/divisor)
        self.__denominator=int(abs(denominator)/divisor)

    def __add__(self,secondRational):
        n=self.__numerator*secondRational[1]+self.__denominator*secondRational[0]
        d=self.__denominator*secondRational[1]
        return Rational(n,d)
    def __sub__(self,secondRational):
        n=self.__numerator*secondRational[1]-self.__denominator*secondRational[0]
        d=self.__denominator*secondRational[1]
        return Rational(n,d)
    def __mul__(self,secondRational):
        n=self.__numerator*secondRational[0]
        d=self.__denominator*secondRational[1]
        return Rational(n,d)
    def __truediv__(self,secondRational):
        n=self.__numerator*secondRational[1]
        d=self.__denominator*secondRational[0]
        return Rational(n,d)
    def __float__(self):
        return self.__numerator/self.__denominator
    def __int__(self):
        return int(self.__float__())

    def __str__(self):
        if self.__denominator==1:
            return str(self.__numerator)
        else:
            #return str(self.__numerator)+"/"+str(self.__denominator)
            return str(self[0])+"/"+str(self[1])

    def __lt__(self, other):
        return self.__cmp__(other) < 0
    def __le__(self, other):
        return self.__cmp__(other) <= 0
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __getitem__(self, item):
        if item==0:
            return self.__numerator
        else:
            return self.__denominator


    def __cmp__(self, other):
        #temp=self.__sub__(other)
        temp=self - other
        if temp[0]>0:
            return 1
        elif temp[0]<0:
            return -1
        else:
            return 0



def gcd(numerator,denominator):
    maxNum= abs(numerator) if abs(numerator) > abs(denominator) else abs(denominator)
    gcd=1
    for i in range(1,maxNum):
        if numerator%i==0 and denominator%i==0:
            gcd=i
    return gcd