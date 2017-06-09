def sort(num1,num2):
    if num1>num2:
        return num1,num2
    else:
        return num2,num1

num1,num2=sort(9,8)
print(num1,num2)