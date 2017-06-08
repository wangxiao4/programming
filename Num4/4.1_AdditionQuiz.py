import random
num1=random.randint(0,100)
num2=random.randint(0,100)
sum=eval(input(str(num1)+"+"+str(num2)+"="))
if(sum==num1+num2):
    print("true")
else:
    print("false")