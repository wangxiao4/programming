sum=0
inputValue=1
valueStr=""
while inputValue!=0:
    inputValue=eval(input("enter a number:\n"))
    if inputValue>0:
        valueStr = valueStr + "+" if valueStr!="" else ""
        valueStr += str(inputValue)
    elif inputValue<0:
        valueStr+=str(inputValue)
    sum+=inputValue

print(valueStr,"=",sum)