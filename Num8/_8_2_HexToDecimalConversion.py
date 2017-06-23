def main():
    hexStr=input("enter a hex string:\n")
    num=hexToDecimal(hexStr)
    print(hexStr,":",num)

def hexToDecimal(hex):
    num=0
    for i in range(0,len(hex)):
        charNum=hex[i]
        num=num*16+hexCharToDecimal(charNum)
    return num

def hexCharToDecimal(ch):
    lowerCh=ch.lower()
    num=0
    if('a'<lowerCh<"z"):
        num=10+ord(lowerCh)-ord('a')
    return num

hexCharToDecimal('d')
main()


