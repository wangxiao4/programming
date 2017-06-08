num1,num2=eval(input("enter tow number\n"))
num_temp=2
greatestCommonDivisor=1
while num_temp <= (num1 if num1<num2 else num2):
    if num1%num_temp == 0 and num2%num_temp==0:
        greatestCommonDivisor=num_temp
    num_temp+=1
print("Greatest Common Divisor is ",greatestCommonDivisor)