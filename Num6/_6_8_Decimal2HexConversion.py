def decimalToHex(devimalvalue):
    Hex=""
    while devimalvalue!=0:
        temp=devimalvalue%16
        Hex=toHexChar(temp)+" "+Hex
        devimalvalue=devimalvalue//16
    return Hex

def toHexChar(num):
    temp=str(num)
    if num>9:
        temp=chr(num-10+ord('a'))
    return temp

devimal=eval(input("enter a number:\n"))
print(decimalToHex(devimal))