#2.1 计算矩形面积
width=10
height=15
area=width*height
print("2.1\n area",area);

#2.2运算后赋值
miles=100
kilometers=miles*1.609
print("2.2\n kilometers is",kilometers)

#2.3提示输入
input_value=input("2.3\n input a value")

#2.4使用eval转换字符失败, 运行式错误
input_number=eval(input("2.4\n input a number"))

#2.5 多行输入
longValue=1+2+3+4+5+6+\
7+8+9

#2.7
'''
    1. 字母 数字 _
    2. 非数字开头
    3. 非关键字
'''

#2.8    2 = a  不能给常量赋值 且 a 未定义
#2.9    0
#2.10   a=2,b=1

#2.11
print("5.1**2",5.1**2)

#2.12 今天周二 100天后周几
print(100%7+2)

#2.13
print(25/4//1)

#2.14
#   4/(3*(r+34))-9*(a+bc)+(3+d*(2+a)/(a+bd))

#2.15
#m*(r**2)

#2.16 假设a=1
#   5   -3  4   0.25    0   1   62

#2.17   应该遵守四舍五入原则  返回最近的整数   int(value)会直接返回小数点前的整数（不会四舍五入）  如果value是浮点数int(value)会改变value的值，强转位整数形
#2.18   正确
#   4   5   22  4   4   运行时错误（不能带有前导0）

#2.19   UNIX系统的发布时间是1970年1月1日 00:00:00
#2.20   返回当前时间与UNIX时间点的时间差，浮点类型值，单位秒，小数点后是微妙
#2.21   time.time()%60
