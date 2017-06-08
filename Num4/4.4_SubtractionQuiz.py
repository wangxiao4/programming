import random
num1=random.randint(0,100)
num2=random.randint(0,100)
answer=eval(input("what is "+str(num1)+"-"+str(num2)+" = ?\n"))
if answer==num1-num2:
    print("true")
else:
    print("false")