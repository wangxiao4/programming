def max(num1,num2):
    return num1 if num1>num2 else num2

num1,num2=eval(input("enter tow number\n"))
print(num1,"、",num2,"比较大的是",max(num1,num2))