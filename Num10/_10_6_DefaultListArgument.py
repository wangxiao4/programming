
#在其他语言中不存在这种现象,(C语言不传递列表地址，情况下)

def add(x,y=[]):
    if x not in y:
        y.append(x)
    return y
def main():
    x=1
    print(add(x))
    x2=2
    print(add(x2))
    x3=add(3,[10,11,12])
    print(x3)
    x4=add(4)
    print(x4)

main()