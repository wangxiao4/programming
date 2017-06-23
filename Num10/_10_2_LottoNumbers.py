isCovered=9*[False]
endOfInput=False
while not endOfInput:
    value=input()
    if eval(value)==0:
        endOfInput=True
    else:
        index=eval(value)-1
        isCovered[index]=True
isTrue=True
for x in isCovered:
    if not x:
        isTrue=x
        break;

if isTrue:
    print("true")
else:
    print("false")