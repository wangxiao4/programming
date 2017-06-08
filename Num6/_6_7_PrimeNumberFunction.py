def isPrime(num):
    temp=True
    for i in range(2,num):
        if num%i==0 and num!=2:
            temp=False
            break
    return temp

def printPrimeNumber(maxNum):
    if maxNum<2:
        return
    colCount=0
    for i in range(2,maxNum):
        if isPrime(i):
            if colCount>9:
                print("\n")
                colCount=0
            print(i,end="\t")
            colCount+=1

num=eval(input("enter max number\n"))
printPrimeNumber(num)