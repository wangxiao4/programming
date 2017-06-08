def gcd(num1,num2):
    temp=2
    for i in range(1,num1 if num2>num1 else num2):
        if num1%i==0 and num2%i==0:
            temp=i
    return temp

#print(gcd(90,66))