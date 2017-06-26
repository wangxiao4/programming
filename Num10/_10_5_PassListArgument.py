def main():
    x=1
    #这里与其他语言存在明显不同 y数组作为main函数的局部变量，调用其他方法对其修改会影响原有数据
    #在其他语言中不存在这种现象，感觉像是bug一样
    y=[1,2,3]
    m(x,y)
    print("x is ",x)
    print("y[0] is ",y[0])

def m(number,numbers):
    number=10
    numbers[0]=10

main()