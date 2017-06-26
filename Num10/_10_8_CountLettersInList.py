from Num6._6_11_RandomCharacter import *
def main():
    list=[0]*100
    letterCount=[0]*26
    for i in range(0,100):
        list[i]=getRandomCharacter('a','z')
    print("原数组：",list)

    for i in range(0,len(list)):
        letterCount[ord('z')-ord(list[i])]+=1

    for x in range(0,26):
        print(chr(ord('a')+x),":",letterCount[x],end="\t")

main()