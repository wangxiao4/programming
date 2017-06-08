num=eval(input("enter input a num\n"))
'''
#渣
if num%2==0 or num%3==0:
    if num%2-num%3==0:
        print(num,"可同时被2、3整除")
    elif num%2-num%3>0:
        print(num,"可被3整除")
    else:
        print(num,"可被2整除")
else:
    print(num,"不能被2、3整除")
'''
if num%2==0 and num%3==0:
    print(num,"可同时被2、3整除")
elif num%2==0 or num%3==0:
    print(num,"可被2或3整除")
else:
    print(num,"不能被2、3整除")